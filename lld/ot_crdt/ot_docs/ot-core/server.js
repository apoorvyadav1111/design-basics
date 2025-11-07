const { WebSocketServer } = require('ws');

class OTServer {
  constructor(port) {
    this.wss = new WebSocketServer({ port });
    this.document = '';
    this.clients = new Set();
    
    this.wss.on('connection', (ws) => this.handleConnection(ws));
    
    console.log(`🚀 OT Server running on ws://localhost:${port}`);
  }

  handleConnection(ws) {
    console.log('✅ Client connected');
    this.clients.add(ws);

    // Send initial document state to the new client
    this.sendMessage(ws, {
      type: 'init',
      content: this.document
    });

    ws.on('message', (data) => {
      try {
        const message = JSON.parse(data);
        this.handleClientMessage(ws, message);
      } catch (err) {
        console.error('Error parsing message:', err);
      }
    });

    ws.on('close', () => {
      console.log('❌ Client disconnected');
      this.clients.delete(ws);
    });

    ws.on('error', (err) => {
      console.error('WebSocket error:', err);
    });
  }

  handleClientMessage(sender, message) {
    if (message.type === 'operation') {
      const op = message.operation;
      
      // Apply operation to server's document
      this.applyOperation(op);
      
      // Broadcast to all OTHER clients (not the sender)
      this.broadcast(sender, {
        type: 'operation',
        operation: op
      });
    }
  }

  applyOperation(op) {
    const pos = op.position;

    // Apply delete first
    if (op.delete) {
      this.document = this.document.slice(0, pos) + 
                      this.document.slice(pos + op.delete);
    }

    // Then apply insert
    if (op.insert) {
      this.document = this.document.slice(0, pos) + 
                      op.insert + 
                      this.document.slice(pos);
    }

    console.log(`📝 Document updated (${this.document.length} chars)`);
  }

  sendMessage(ws, message) {
    if (ws.readyState === 1) { // OPEN
      ws.send(JSON.stringify(message));
    }
  }

  broadcast(sender, message) {
    this.clients.forEach((client) => {
      if (client !== sender && client.readyState === 1) {
        this.sendMessage(client, message);
      }
    });
  }
}

// Start the server
new OTServer(8080);
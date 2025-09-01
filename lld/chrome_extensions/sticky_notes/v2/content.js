/**
 * Global variable to store notes data for the current page.
 * @type {Array<Object>}
 */
let notes = [];

/**
 * Loads notes from local storage and displays them on the webpage.
 * The notes are stored with a key that is a combination of the URL and the parent element's ID.
 */
function loadNotes() {
    const url = window.location.href;
    const notesData = localStorage.getItem(`notes_${url}`);
    if (notesData) {
        notes = JSON.parse(notesData);
        notes.forEach(note => {
            displayNote(note);
        });
    }
}

/**
 * Finds the nearest parent element with an ID to serve as a stable anchor for the note.
 * This ensures the note can be reloaded accurately even if the page structure changes slightly.
 * @param {HTMLElement} element - The starting element (e.g., the selected text's parent).
 * @returns {HTMLElement|null} The nearest parent element with an ID, or null if not found.
 */
function findParentWithId(element) {
    let currentElement = element;
    while (currentElement && !currentElement.id) {
        currentElement = currentElement.parentElement;
    }
    return currentElement;
}

/**
 * Creates and displays a note on the webpage.
 * @param {Object} note - The note object containing text, position, and color.
 * @param {boolean} isNew - Flag to indicate if this is a new note being created.
 */
function displayNote(note, isNew = false) {
    const parentElement = document.getElementById(note.parentId);
    if (!parentElement) {
        console.error("Parent element not found for note:", note);
        return;
    }

    const noteElement = document.createElement('div');
    noteElement.className = 'sticky-note';
    noteElement.style.backgroundColor = note.color;
    noteElement.style.top = `${note.y}px`;
    noteElement.style.left = `${note.x}px`;

    if (isNew) {
        // Define the color palette
        const colors = ['#ffff80', '#e0b0ff', '#80ff80', '#a0c7ff', '#ff8080'];
        const colorSwatchesHTML = colors.map(color => `<div class="color-swatch" style="background-color:${color};" data-color="${color}"></div>`).join('');

        noteElement.innerHTML = `
            <textarea placeholder="Write your note here..."></textarea>
            <div class="note-controls">
                <div class="color-palette">${colorSwatchesHTML}</div>
                <button class="save-note">Save</button>
            </div>
        `;
        parentElement.appendChild(noteElement);

        const saveButton = noteElement.querySelector('.save-note');
        const colorPalette = noteElement.querySelector('.color-palette');
        const textarea = noteElement.querySelector('textarea');

        // Set initial color
        let selectedColor = colors[0];
        noteElement.style.backgroundColor = selectedColor;

        // Listen for color swatch clicks
        colorPalette.addEventListener('click', (e) => {
            const swatch = e.target.closest('.color-swatch');
            if (swatch) {
                selectedColor = swatch.dataset.color;
                noteElement.style.backgroundColor = selectedColor;
            }
        });

        // Listen for save button click
        saveButton.addEventListener('click', () => {
            if (textarea.value.trim() !== '') {
                const newNote = {
                    text: textarea.value,
                    color: selectedColor,
                    parentId: note.parentId,
                    x: note.x,
                    y: note.y
                };
                notes.push(newNote);
                saveNotes();
                noteElement.remove();
                displayNote(newNote);
            } else {
                noteElement.remove();
            }
        });
        textarea.focus();
    } else {
        noteElement.innerHTML = `
            <p>${note.text}</p>
            <span class="note-close">&times;</span>
        `;
        parentElement.appendChild(noteElement);

        noteElement.querySelector('.note-close').addEventListener('click', () => {
            noteElement.remove();
            notes = notes.filter(n => n.text !== note.text || n.color !== note.color);
            saveNotes();
        });
    }
}

/**
 * Saves the current state of notes to local storage.
 */
function saveNotes() {
    const url = window.location.href;
    localStorage.setItem(`notes_${url}`, JSON.stringify(notes));
}

// Listen for text selection
document.addEventListener('mouseup', (event) => {
    const selectedText = window.getSelection().toString().trim();
    if (selectedText.length > 0) {
        const parentElement = findParentWithId(event.target);
        if (parentElement && parentElement.id) {
            // Create a temporary note object for position and parent tracking
            const tempNote = {
                parentId: parentElement.id,
                x: event.clientX + window.scrollX,
                y: event.clientY + window.scrollY
            };
            displayNote(tempNote, true); // True flag indicates it's a new note
        } else {
            console.warn("Could not find a parent element with a stable ID. Note creation aborted.");
        }
    }
});

// Initial load of notes when the page loads
loadNotes();
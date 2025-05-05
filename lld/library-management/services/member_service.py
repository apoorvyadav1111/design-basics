from entities.enums import MembershipStatus
from entities.member import Member


class MemberService:
    def __init__(self):
        self.members = {}

    def create_member(self, name: str, age: str, gender: str):
        new_member = Member(name, age, gender)
        self.members[new_member._id] = new_member
        return new_member

    def get_member(self, member_id: str):
        return self.members.get(member_id, None)
    
    def __update_membership_status(self, member_id: str, status: MembershipStatus):
        member = self.get_member(member_id)
        if member:
            member.update_membership_status(status)
            return member
        return None
    
    def deactivate_member(self, member_id: str):
        return self.__update_membership_status(member_id, MembershipStatus.INACTIVE)
    
    def activate_member(self, member_id: str):
        return self.__update_membership_status(member_id, MembershipStatus.ACTIVE)
    
    def suspend_member(self, member_id: str):
        return self.__update_membership_status(member_id, MembershipStatus.SUSPENDED)
    
    def rename_member(self, member_id: str, new_name: str):
        member = self.get_member(member_id)
        if member:
            member.name = new_name
            return member
        return None
    
    def delete_member_permanently(self, member_id: str):
        if member_id in self.members:
            del self.members[member_id]
            return True
        return False
    
    
    


    

    

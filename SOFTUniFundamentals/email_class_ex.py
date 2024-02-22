class Email:
    def __init__(self, sender, receiver, content):
        self.is_sent = False
        self.sender = sender
        self.receiver = receiver
        self.content = content

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"

info = input()
info_list = []
while info != "Stop":
    info_list.append(info)
    info = input()

info_list_split = [num.split() for num in info_list]
numbers = [int(num) for num in input().split(", ")]

for i in range(len(info_list)):
    conversation = Email(sender= info_list_split[i][0],receiver= info_list_split[i][1],content= info_list_split[i][2])
    if i in numbers:
        conversation.send()
        print(conversation.get_info())
    else:
        print(conversation.get_info())
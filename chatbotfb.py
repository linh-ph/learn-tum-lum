# Để tạo một chatbot cho Facebook sử dụng Python, 
# bạn có thể sử dụng Facebook Messenger API và một số thư viện Python như python-telegram-bot hoặc fbchat.

# Để bắt đầu, bạn cần có một tài khoản Facebook và một trang Facebook. 
# Sau đó, bạn cần tạo một ứng dụng Facebook và lấy mã truy cập cho trang của bạn từ ứng dụng đó.

# Sau khi có mã truy cập, bạn có thể sử dụng một trong những thư viện để tạo chatbot. 
# Ví dụ, với fbchat, bạn có thể lấy mã sau đây để tạo một chatbot đơn giản:
# ////
from fbchat import Client
from fbchat.models import *

class EchoBot(Client):
    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsRead(author_id)
        self.send(Message(text=message_object.text), thread_id=thread_id, thread_type=thread_type)

client = EchoBot("<email>", "<password>")
client.listen()
# ////
# Trong đoạn mã trên, EchoBot là một lớp kế thừa từ Client của fbchat. 
# Lớp này có một phương thức onMessage() được gọi mỗi khi có một tin nhắn mới đến. 
# Phương thức này sẽ đánh dấu tin nhắn đó là đã đọc và gửi lại nội dung của tin nhắn đó cho người gửi.
# Cuối cùng, bạn có thể khởi tạo một đối tượng ứng với EchoBot và gọi phương thức listen() 
# để bắt đầu lắng nghe các tin nhắn đến. Khi có một tin nhắn mới, 
# phương thức onMessage() sẽ được gọi và chatbot sẽ gửi lại nội dung của tin nhắn đó cho người gửi.
# Bạn cũng có thể tùy chỉnh hành vi của chatbot bằng cách thêm một số lệnh điều khiển vào trong phương thức onMessage(). 
# Ví dụ, bạn có thể thêm một điều kiện để chatbot chỉ gửi lại tin nhắn nếu nội dung của tin nhắn bắt đầu bằng cụm từ "echo":
# /////
def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsRead(author_id)
        if message_object.text.startswith("echo"):
            self.send(Message(text=message_object.text), thread_id=thread_id, thread_type=thread_type)
# /////
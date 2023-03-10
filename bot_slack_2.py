import openai
import slack

openai.api_key = "your_openai_api_key"
slack_client = slack.WebClient(token="your_slack_bot_token")

def chatbot_response(text):
  model_engine = "text-davinci-002"
  prompt = (f"{text}")

  completions = openai.Completion.create(
      engine=model_engine,
      prompt=prompt,
      max_tokens=2048,
      n=1,
      stop=None,
      temperature=0.7,
  )

  message = completions.choices[0].text
  return message

@slack_client.on("message")
def handle_message(event):
  message = event["text"]
  response = chatbot_response(message)
  slack_client.chat_postMessage(channel="#general", text=response)

slack_client.start()

/*Trong đoạn mã này, chúng ta sử dụng các thư viện openai và slack để kết nối và giao tiếp với ChatGPT của OpenAI và Slack. Chúng ta cũng đã tạo một hàm chatbot_response() để lấy câu trả lời từ ChatGPT và một hàm xử lý sự kiện message để nhận tin nhắn từ Slack và gửi câu trả lời về.

Để sử dụng đoạn mã này, hãy thay thế "your_openai_api_key" và "your_slack_bot_token" bằng API key của bạn từ OpenAI và Slack, sau đó chạy đoạn mã này bằng Python. Sau đó, bạn có thể gửi tin nhắn đến kênh Slack của bạn và nhận được câu trả lời từ ChatGPT qua Slack.*/
// Gửi yêu cầu tới API của ChatGPT
fetch('https://api.openai.com/v1/engines/davinci-codex/completions', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_API_KEY'
    },
    body: JSON.stringify({
        prompt: 'YOUR_PROMPT',
        temperature: 0.5,
        max_tokens: 2048,
    }),
}).then(response => response.json())
.then(data => {
    // Xử lý kết quả trả về từ API
    console.log(data);
});

// Hiển thị kết quả trả về từ API trong một thẻ div
document.getElementById("chatbot-response").innerHTML = data.choices[0].text;

///////
const axios = require('axios');

const GPT3_API = 'https://api.openai.com/v1/engines/davinci/completions';

axios.post(GPT3_API, {
  prompt: 'What is the weather like today?',
  api_key: OPENAI_KEY
}).then(response => {
  console.log(response.data);
}).catch(error => {
  console.log(error);
});

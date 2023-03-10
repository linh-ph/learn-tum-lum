const { WebClient } = require('@slack/web-api');
const client = new WebClient('xoxb-1519108534465-4625339132438-3AOzQVWAKw5zPcw2BeVl2O4z');

client.conversations_list().then(response => {
  console.log(response);
});

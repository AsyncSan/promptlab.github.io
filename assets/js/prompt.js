
function queryAPI(url, authorization, org) {
    const xhr = new XMLHttpRequest();
    xhr.onreadystatechange = function() {
      if (this.readyState == 4 && this.status == 200) {
        // Process response
        console.log(this.responseText);
      }
    };
    xhr.open("GET", url, true);
    xhr.setRequestHeader("Authorization", authorization);
    xhr.setRequestHeader("OpenAI-Organization", org);
    xhr.send();
  }
  
  queryAPI("https://api.openai.com/v1/models", "Bearer YOUR_API_KEY", "org-reyhJK05Ya3s4pyJG4zMBe7r");
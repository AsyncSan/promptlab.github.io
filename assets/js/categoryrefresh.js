window.onload = function () {
    document.getElementById('categoryButton').addEventListener('click', function(){
        console.log("CLicked the button categoryButton");
    });

    function goTo(url) {
        window.location.href = url;
      }

    function fetchPosts(category){
        $.ajax({
            url: '/category/' + category,
            success: function(data) {

            },
            complete: function(datu) {
                // this callback is called when the response is ready
                // code to parse HTML and extract posts
                console.log(datu);
                                // find the element with the id "postList"
                                var postList = document.getElementById("postList");
                                console.log("postlist: "+ postList);
                                console.log(JSON.stringify(datu));
                                
                                // parse the HTML response and find the posts
                                var parser = new DOMParser();
                                var doc = parser.parseFromString(datu, "text/html");
                                var posts = doc.getElementsByClassName("post");
                    
                                // for each post, create a <li> element and add it to the postList
                                for (var i = 0; i < posts.length; i++) {
                                  var post = posts[i];
                                  var postTitle = post.getElementsByTagName("h2")[0].innerHTML;
                                  var postLink = post.getElementsByTagName("a")[0].href;
                    
                                  var listItem = document.createElement("li");
                                  listItem.innerHTML = `<a href="${postLink}">${postTitle}</a>`;
                                  postList.appendChild(listItem);
                                }
            }
        });
    }
    $('#myButton').on('click', function(){
        var category = $(this).data('category');
        console.log(category);
        fetchPosts(category);
    });

    /*
    function fetchPosts(category){
        $.ajax({
            url: '/category/' + category,
            success: function(data) {
                console.log(JSON.stringify(data));
                var posts = $(data).find('.post');
                var postList = $('#postList');
                postList.html('');
                posts.each(function(index, element) {
                    postList.append(
                        `<li><a href="${$(element).find('a').attr('href')}">${$(element).find('.post-title').text()}</a></li>`
                    );
                });
            }
        });
    }
    $('#myButton').on('click', function(){
        var category = $(this).data('category');
        console.log(category);
        fetchPosts(category);
    });
*/
/*
    //Füge ein Event hinzu, das auf das Klicken des Buttons reagiert
document.getElementById('myButton').addEventListener('click', function() {
    let posts = fetch('/category/' + this.dataset.category);
    console.log(JSON.stringify(posts));
    posts.then(function(response) {
        console.log(JSON.stringify(response));
        response.json().then(function(data) {
            console.log(JSON.stringify(data));
            let postList = document.getElementById('postList');
            postList.innerHTML = '';
            data.posts.forEach(function(post) {
                postList.innerHTML += `<li><a href="${post.url}">${post.title}</a></li>`;
            });
        });
    });
});
*/
};
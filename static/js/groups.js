console.log("Hello")


function add_comment(comment){
    comments = document.querySelector('#comments')
    new_comment = `
        <div style="display: flex; justify-content: flex-end">
                            <div class="comment">
                                <small><i>${user_full_name}</i></small>
                                <p>${comment}</p>
                            </div>
        </div>
    `
    comments.innerHTML += new_comment
}
function send_comment(id){
    comment = document.querySelector('#write_commit').value
    url = `/comment/${id}`
    request = new Request(
        url,
        {
            method : 'POST',
            headers : {'X-CSRFToken': csrftoken},
            body : JSON.stringify({
                'comment' : comment
            })
        }
    )
    fetch(request)
        .then((response) => {
            console.log(response)
            if(response.status == 201){
                add_comment(comment)
            }
    })

}
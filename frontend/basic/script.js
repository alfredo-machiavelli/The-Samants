//bound to button onclick

function userLoggedIn(){
    //get the value in the input element
    let userInput = document.getElementById("Username").value
    let userPassword = document.getElementById("Password").value
    //change the inner HTML of the adjective (span) element
    document.getElementById('text-box').innerHTML = userInput + " is in the system"
        //call login function in login.py
        //if error then print errorMsg
}

function SignUp()
{
  let userInput = document.getElementById("Username").value
    let userPassword = document.getElementById("Password").value
    //call singupfunction in login.py
    //if error then print errorMsg
}


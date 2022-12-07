//  Verify all the users

function verify_user(all_userx, usernamex){
  // Iterate throughout all_users (list)
  // If the name exists in the database return true
  //console.log(usernamex);
    let num = 0;
    
    for(let i in all_userx){
      if(usernamex == all_userx[i]){
        //console.log('Match') verify
        num += 1;
        break;
      }
    }
    //console.log(num);
    if(num > 0){
      return true; // true == theres a match
    }else{
      return false;
    }
  
}

// Verify all the email addresses
function verify_email(mailxs, email){
  // Iterate throughout all_users (list)
  // If the name exists in the database return true
  //console.log(usernamex);
    let num = 0;
    //console.log(mailxs);
    //console.log(email);
    for(let i in mailxs){
      if(email == mailxs[i]){
        //console.log('Match') verify
        num += 1;
        break;
      }
    }
    //console.log(num);
    if(num > 0){
      return true; // true == theres a match
    }else{
      return false;
    }
  
}

function signup(userz, mailxs){ 
  // Note: userz is the string with all the user data from flask (python file)
    // Why are we doing this instead of list? In javascript you cannot pass an array with lists from html to javascript only arrays with numbers. As a result i had to convert the array in python to a string, then ima do a javascript split in order to get an array
    // Get all the values from the form 
    //console.log(userz);
    let all_users = userz.split(" "); // Spit based on the spaces and convert to array
    let all_emails = mailxs.split(" "); 
    // Code below used to verify
    //console.log(all_users);
    //console.log(typeof(all_users));
  //alert(mailxs)
    firstName = fname.value;
    lastName = lname.value;
    email = email.value;
    password = password.value;
    confirm_password = confirm_password.value;
    username = username.value;
    // Do a forloop
    let total_value = 1; // use this in order to see if the user's username already exists
    
    //alert(firstName + " " + lastName + " " + email + " " + password + " " + confirm_password + " " + username); Confirm if all the values are got! 
    // Convert to dictionary
    
    // Template for the if statements
    /* 
      firstName / LastName = atleast 2 characters
      email: must contain @ and greater than 3 characters
      username: atleast 4 characters, max of 8 characters
      password: contain atleast 8 characters and matches with password_verification

      Start with firstName and lastName
    */
    // Check if everything is filled out
    
    
    if(firstName.length == 0 || lastName.length == 0 || email.length == 0 || username.length == 0 || confirm_password.length == 0 || confirm_password.length == 0){
      
      alert("Fill out everything please");
      location.reload(); // reload the page if there is issues
      //window.location.replace("/signup"); // refresh the page
    }
    else if(firstName.length < 3 || lastName.length < 3){ // if less than 3 characters
      alert("Make sure both first name and last name are over 2 characters");
      location.reload(); // reload the page if there is issues
    }
    else if(email.length < 7){
      alert("Make email length greater than 6 characters");
      location.reload(); // reload the page if there is issues
    }
    else if(verify_email(all_emails, email)){
      alert("Your email is not unique, please use a different email address");
      location.reload(); // reload the page if there is issues
    }
    else if(email.indexOf(' ') >= 0){
      alert("Make sure the email has no spaces, includes if you have spaces after the last character")
      location.reload(); // reload the page if there is issues
    }
    else if(username.length < 4 || username.length > 16){
      //alert(username.length);
      alert("Make sure username is in between 4 - 15 Characters");
      location.reload();
    }
    // If theres any space in the username
    else if(username.indexOf(' ') >= 0){
      alert("Make sure username has no spaces, includes if you have spaces after the last letter")
      location.reload(); // reload the page if there is issues
    }
    else if(password.length < 8){
      alert('Make sure password is at least 8 characters');
      location.reload(); // reload the page if there is issues
    }
    // If both passwords are not the same
    else if(password != confirm_password){
      alert('Make sure both passwords are the same');
      location.reload();
    }
    // using verify_user function which takes 2 parameters, will call the function at the top, the function at the top returns a boolean value
    else if(verify_user(all_users, username)){
      alert("Username already in use, please use a new username");
      location.reload(); // reload the page if there is issues
      
    }
  
    else {
      //fetch(options).then(res => res.json()).then(data=> console.log(data))
    var entry = {
      Fname: firstName,
      Lname: lastName,
      email: email,
      password: password,
      username: username
  } // the fetch api will send json data containing our users information to the python file where everything will be put into the database!. In python it will convert the JavaScript json to a python dictionary
    fetch ('/signup', {
        method : "POST",
        credentials : 'include',
        body : JSON.stringify(entry),
        cache : "no-cache",
        headers : new Headers ({
          "content-type" :"application/json"
       })
     }).then(window.location.replace("/home"))}


}
function signup(userz){ 
    // Get all the values from the form 
    firstName = fname.value;
    lastName = lname.value;
    email = email.value;
    password = password.value;
    confirm_password = confirm_password.value;
    username = username.value;
    // Do a forloop
    let total_value = 1; // use this in order to see if the user's username already exists
    console.log(userz);
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
    else if(username.length < 4 || username.length > 16){
      //alert(username.length);
      alert("Make sure username is in between 4 - 15 Characters");
      location.reload();
    }
    else if(username.indexOf(' ') >= 0){
      alert("Make sure username has no spaces")
      location.reload(); // reload the page if there is issues
    }
    else if(password.length < 8){
      alert('Make sure password is at least 8 characters');
      location.reload(); // reload the page if there is issues
    }
    else if(password != confirm_password){
      alert('Make sure both passwords are the same');
      location.reload();
    }
    
  
    else {
    var entry = {
      Fname: firstName,
      Lname: lastName,
      email: email,
      password: password,
      username: username
  }
    fetch ('/signup', {
        method : "POST",
        credentials : 'include',
        body : JSON.stringify(entry),
        cache : "no-cache",
        headers : new Headers ({
          "content-type" :"application/json"
       })
     })}


    
/*
 // If statement for signup
 (fetch('/signup')
 .then(function (response) { // create response
     return response.text(); // return the text gotten from python
 }).then(function (text) {
     console.log('GET response text:');
     console.log(text); // Print the greeting as text
 }))/*{
   window.location.replace("/home");} // Change location to home*/ 

}
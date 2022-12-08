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
     }).then(alert("Congrats you have signed up and made an account! " + username)).then(window.location.replace("/home"))}


}

function hi(username){
  alert("Welcome " + username + " to the journey!");
}


function change() {
  document.body.style.backgroundColor = "white";
  document.body.style.Color = "black";
  document.getElementById("live").style.color = "black";
}


document.getElementById("work").addEventListener("mouseover",changeTextA)
document.getElementById("work").addEventListener("mouseout",changeTextOutA)



  function description(x){

    if(x==1){
    document.getElementById("work").innerHTML="<p>What does work on this website mean? It means that you can download the github repo (Check line 7)for this project and add features! Make sure to send these features to, biswassudiptto@gmail.com, and we will add them. This will help you for experience. We may also email you tasks to do for the website (optional). Great way to get experience</p>";

    document.getElementById("repo").innerHTML = "<a href='https://github.com/Sudiptto/CsOpportunities'>Click to access the github repo for this website</a>"}
    else if(x==2){
      document.getElementById("project").innerHTML = "Work on projects to gain experience: In the opportunities/internship section, users can list projects and you can do these projects for credit! Just make sure to email to contact biswassudiptto@gmail.com and the user who gave the project idea that you are doing the project. If you do the project and have proof than you will earn credit. Check the contact section for more information"
    }
  }

  function og(x){
    if(x==1){
    document.getElementById("work").innerHTML= "Work on this website!";}
    else if(x==2){
      document.getElementById("project").innerHTML = "Work on projects!"
    }

  }

// FUNCTIONS BELOW ARE FOR SENDING UPLOAD DATA TO PYTHON

function send(){
  //alert('hi');
  title = title.value;
  duration = dayz.value;
  date = whichdate.value;
  paid = money.value; // paid per hour
  description = desc.value;

  //alert(title + " " + duration + " " + date + " " + paid + " " + description)
  //alert(typeof(date))
  //alert(typeof(paid)) always returns a string
  // Start the IF STATEMENTS
  if(title.length == 0 || duration.length == 0 || paid.length == 0 || date.length == 0 || description.length == 0){
    alert('Please fill out everything!')
    location.reload();
  }
  else if(title.length <= 3 || title.length > 490){
    alert('Please make the title length between 4 - 490 characters!');
    location.reload();
  }
  else if(description.length <= 19 || description.length > 8000){
    alert('Please make the description length between 20 - 8000 characters')
  }
  
  else{
    var entry = {
      title: title,
      duration: duration,
      date: date,
      paid: paid,
      description: description
  }
    fetch ('/upload', {
      method : "POST",
      credentials : 'include',
      body : JSON.stringify(entry),
      cache : "no-cache",
      headers : new Headers ({
        "content-type" :"application/json"
     })
   })
   alert('Added')
   location.reload()
  }
  


}

function deleteEvent(noteId) {
  fetch("/delete-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId }),
  }).then((_res) => {
    window.location.href = "/upload";
  });
}
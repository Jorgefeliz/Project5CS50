document.addEventListener('DOMContentLoaded', function() {

    document.querySelector('#home').style.display = 'block';
    document.querySelector('#event').style.display = 'none';
    document.querySelector('#issue').style.display = 'none';
    document.querySelector('#payment').style.display = 'none';

   
    
  });

function alerta(){

    alert("You haven't pay")

}

function home (){

    document.querySelector('#home').style.display = 'block';
    document.querySelector('#event').style.display = 'none';
    document.querySelector('#issue').style.display = 'none';
    document.querySelector('#payment').style.display = 'none';
 
    
}

function schedule (){

   
    document.querySelector('#home').style.display = 'none';
    document.querySelector('#event').style.display = 'block';
    document.querySelector('#issue').style.display = 'none';
    document.querySelector('#payment').style.display = 'none';

    document.querySelector("#event").innerHTML = `
        <h3> Event scheduler </h3>
        <p> Please note that no loud music is allowed (>80db from entrance) </p>

        <form id="event_form"  onsubmit="return schedule_event()">

            <label for="event">Event:</label>
                <select id="event_type" name="event_type">
                    <option value="birthday">Birthday</option>
                    <option value="meeting">Business/family meeting</option>
                    <option value="other">Others</option>
                </select>
                <br>

            <label for="place">Place:</label>
                <select id="place" name="place">
                    <option value="gazebo1">Gazebo 1</option>
                    <option value="gazebo2">Gazebo 2</option>
                    <option value="court">basketball court</option>
                </select>
                <br>

            <label for="date">Date:</label>
            <input type="date" id="date" name="date">
            <br>

            <input type="submit" value="Submit">
        </form>    `;
}

function issue (){

    document.querySelector('#home').style.display = 'none';
    document.querySelector('#event').style.display = 'none';
    document.querySelector('#issue').style.display = 'block';
    document.querySelector('#payment').style.display = 'none';

    document.querySelector("#issue").innerHTML = `
   
    <h3> Issue Report </h3>
  
    <form id="issue_form"  onsubmit="return issue_report()">

         <label for="title">Title:</label>
         <input type="text" placeholder="title" name="title" id="issue_title" required>

        <label for="issue">Issue Type:</label>
            <select id="issue_type" name="issue_type">
                <option value="water">Water</option>
                <option value="electricity">Electricity</option>
                <option value="sound">Loud sound</option>
                <option value="construction">construction</option>
                <option value="other">Other</option>
            </select>
            <br>
        <label for="description">Description:</label>
        <textarea id="description_issue"></textarea>

        <br>

        <input type="submit" value="Submit">
    </form>   
    `;
}

function announcement (){

    document.querySelector('#home').style.display = 'none';
    document.querySelector('#event').style.display = 'none';
    document.querySelector('#issue').style.display = 'none';
    document.querySelector('#payment').style.display = 'block';
    

}

function schedule_event() {
    
    const event_type = document.querySelector('#event_type').value;
    const place = document.querySelector('#place').value;
    const date = document.querySelector('#date').value;

    
    fetch('/event', {
      method: 'POST',
      body: JSON.stringify({
        event_type: event_type,
        place: place,
        date: date
          
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
   
        console.log(result);
        alert(result["message"])
    });
  localStorage.clear();
  return false;
 
}


// Admin function
function event_update(event_id ) {
    
    let evento =  "event" + event_id
    const event_status = document.getElementById(evento);
    evento = event_status.options[event_status.selectedIndex].text;

    let route = '/event/' + event_id + '/' + evento 
    fetch(route)
    .then(response => response.json())
    .then(result => {
        // Print result
   
        console.log(result);
     
    });
  evento = "row" + event_id
  document.getElementById(evento).style.display = 'none';
  localStorage.clear();
  return false;
 
}

// Admin function
function announcement_post(){
 
    const title = document.querySelector('#title').value;
    const content = document.querySelector('#content').value;
    const valid_date = document.querySelector('#valid_date').value;

    fetch('/announcement', {
        method: 'POST',
        body: JSON.stringify({
          title: title,
          content: content,
          valid_date: valid_date
            
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
     
          console.log(result);
          alert(result["message"])
          window.location.href = '/'
      });
    localStorage.clear();

    document.querySelector('#title').value = "";
    document.querySelector('#content').value = "";
    document.querySelector('#valid_date').value = "";




    return false;
    
}

function announce_delete(announce_id){
 
    let route = '/announcement_update' 
    fetch(route, {
        method: 'PUT',
        body: JSON.stringify({
            announce_id: announce_id
            
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
     
          console.log(result);
          alert(result["message"])
      });
    localStorage.clear();

    route = 'announce' + announce_id
    document.getElementById(route).style.display = 'none';

    return false;
    
}

function announce_edit(announce_id){
 
    let route = '/announcement_retrieve' 
    fetch(route, {
        method: 'POST',
        body: JSON.stringify({
            announce_id: announce_id
            
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
     
          console.log(result);

          route = 'announce' + announce_id
          document.getElementById(route).innerHTML = `

          <form id="announce_edit"  onsubmit="return announce_save(${announce_id})">
          <label for="title"><b>Title:</b></label>
          
          <textarea id="title${announce_id}"> ${result['title']} </textarea>

          <textarea id="text${announce_id}"> ${result['content']} </textarea>

          <label for="previous_valid"><b>Actual valid date: ${result['valid_date']}</b></label> <br>
          <label for="date">Date:</label>
          <input type="date" id="date${announce_id}" name="date" placeholder="${result['valid_date']}" requiered ><br>
          <input type="submit" class="btn btn-primary"  value="Save"  />
          <input type="button" class="btn btn-warning"  value="Cancel" onclick="announce_cancel( ${announce_id} )" />
          <br>
          <br>
          <hr>
          </form>
     
          `;
         
      });
    localStorage.clear();

 

    return false;
    
}

function announce_save(announce_id){
 
    let id = "title"+ announce_id;
  
    const title = document.getElementById(id).value;

    id = "text"+ announce_id
    const content = document.getElementById(id).value;

    id = "date" + announce_id
    const valid_date = document.getElementById(id).value;

    fetch('/announcement_update', {
        method: 'POST',
        body: JSON.stringify({
          announce_id: announce_id,
          title: title,
          content: content,
          valid_date: valid_date
            
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
     
          console.log(result);
     
 
      });
    
    // I will make sure that I only show the values in database
    announce_cancel(announce_id)
   //document.location.reload(true)
   //window.location.href = '/'

}

function announce_cancel(announce_id){

    let route = '/announcement_retrieve' 
    fetch(route, {
        method: 'POST',
        body: JSON.stringify({
            announce_id: announce_id
            
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
     
          console.log(result);

    
    id = 'announce' + announce_id
    document.getElementById(id).innerHTML = `
    <h4> ${result['title']} </h4>
    <p> ${result['content']} </p>
    <em> ${result['valid_date']}</em><br>
    <input type="button" class="btn btn-primary"  value="Edit" onclick="announce_edit( ${announce_id})" />
    <input type="button" class="btn btn-warning"  value="Delete" onclick="announce_delete( ${announce_id})" />
    <br>
    <br>
    <hr>
    `;
     });
    localStorage.clear();
}

function issue_report(){
    const title = document.querySelector('#issue_title').value;
    const categoria = document.querySelector('#issue_type').value;
    const description = document.querySelector('#description_issue').value;
    const status = "pending";

    
    fetch('/issue/0', {
      method: 'POST',
      body: JSON.stringify({
        title :title,
        categoria: categoria,
        description: description,
        status: status
          
      })
    })
    .then(response => response.json())
    .then(result => {
        // Print result
        alert(result["message"])
    });
  window.location.href = '/'
  localStorage.clear();
  return false;
}

function issue_update(issue_id){

    let issue =  "issue" + issue_id
    const issue_status = document.getElementById(issue)
    issue = issue_status.options[issue_status.selectedIndex].text;

    fetch('/issue/0', {
        method: 'PUT',
        body: JSON.stringify({
          id: issue_id,
          status: issue
            
        })
      })
      .then(response => response.json())
      .then(result => {
          // Print result
          alert(result["message"])
      });
    window.location.href = '/'
    localStorage.clear();
    return false;
}

function issue_view(issue_id){

    let route = '/issue/' + issue_id
    fetch(route)
    .then(response => response.json())
    .then(result => {
        // Print result
   
        console.log(result);
        
        route = "detail" + issue_id
        document.getElementById(route).style.display = "block";
        document.getElementById(route).innerHTML =`
        <ul>
            <li> Ticket number: ${result["id"]} </li>
            <li> Title: ${result["title"]} </li>
            <li> Category: ${result["categoria"]} </li>
            <li> Description: </li>
            <li> ${result["description"]} </li>

            <li> Reported: ${result["reported_date"]} </li>
            <li> Status: ${result["status"]} </li>
            <input type="button" class="btn btn-secondary"  value="Close" onclick="close_form(  ${issue_id} )" />
        </ul>
        `;

     
    });
  
    localStorage.clear();
    return false;
}
  
  function close_form(issue_id) {
    let issue = "detail" + issue_id
    document.getElementById(issue).style.display = "none";
  }


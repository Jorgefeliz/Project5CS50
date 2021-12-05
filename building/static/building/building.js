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
}

function payment (){

    document.querySelector('#home').style.display = 'none';
    document.querySelector('#event').style.display = 'none';
    document.querySelector('#issue').style.display = 'none';
    document.querySelector('#payment').style.display = 'block';
}

function schedule_event() {
    alert("You haven't pay")
    const event_type = document.querySelector('#event_type').value;
    const place = document.querySelector('#place').value;
    const date = document.querySelector('#date').value;

    console.log(place);
    console.log(date);

    
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
    });
  localStorage.clear();
  return false;
 
}



const container = document.querySelector('.seatcontainer ');
// const disabled = document.querySelectorAll('.row .seat:not(.disabled)');
const allseats = document.querySelectorAll('.row-seat .seat');
const seats = document.querySelectorAll('.row-seat .seat:not(.occupied)');
const count = document.getElementById('count');
const total = document.getElementById('total');


// console.log(trip_cost)
populateUI();


// //Update total and count
function updateSelectedCount() {
    const selectedSeats = document.querySelectorAll('.row-seat .seat.selected');

    const seatsIndex = [...selectedSeats].map(function (seat) {
        return [...seats].indexOf(seat)+1;
    });

    // const seatsIndex = [...selectedSeats].map(seat => [...allseats].indexOf(seat)+1);

    console.log(typeof(seat));
    // seatsIndex = seatsIndex + 1
    localStorage.setItem('selectedSeats', JSON.stringify(seatsIndex));

    const selectedSeatsCount = selectedSeats.length;

    count.innerText = selectedSeatsCount;
    total.innerText = selectedSeatsCount * trip_cost;
    

}

//get data from localstorage and populate the ui
function populateUI() {
    const selectedSeats = JSON.parse(localStorage.getItem('selectedSeats'));
    console.log(selectedSeats)
    
    
    if (selectedSeats !== null && selectedSeats.length > 0) {
        seats.forEach((seat, index)=> {
          if (selectedSeats.indexOf(index+1) > -1) {
            console.log(selectedSeats.indexOf(index+1))
            seat.classList.add('selected');
          }
        });
    }

}

container.addEventListener('click', (e) => {
    
    if(e.target.classList.contains('seat') && !e.target.classList.contains('occupied')) {
        if(e.target.classList.contains('driver')){
            return false
        }else{
        e.target.classList.toggle('selected');
        const selectedSeats = document.querySelectorAll('.row-seat .seat.selected');
        const selectedSeatsCount = selectedSeats.length;
        console.log(document.getElementsByClassName('driver'))
        if (selectedSeatsCount > 3) {
            e.target.classList.toggle('selected');
            document.getElementById('alrt').innerHTML='Only 3 seats/booking. <br>Finish and book again for more seats'; 
            setTimeout(function() {document.getElementById('alrt').innerHTML='';},5000);
            // alert("you cant only book 3 seats per booking")
            return false
        }
    }
    }

    updateSelectedCount();
});

updateSelectedCount();
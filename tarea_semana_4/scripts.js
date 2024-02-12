//Ejercicios click   
var EventoClick1 = document.getElementById("EClick1");
var EventoClick2 = document.getElementById("EClick2");
var EventoClick3 = document.getElementById("EClick3");

EventoClick1.addEventListener("click",EventoClick1_action)
EventoClick2.addEventListener("click",EventoClick2_action)
EventoClick3.addEventListener("click",EventoClick3_action)

function EventoClick1_action(){
    EventoClick1.textContent = "Haz escrito en la textbox:"+EventoClick2.value
    console.log("El evento se ha activado");
}
function EventoClick2_action(){
    EventoClick2.placeholder = "";
    console.log("El evento se ha activado")
}
function EventoClick3_action(){
    EventoClick3.textContent = "Hola!, me has atrapado"
}

//Ejercicios Focus
var EventoFocus1 = document.getElementById("EFocus1");
var EventoFocus2 = document.getElementById("EFocus2");
var EventoFocus3 = document.getElementById("EFocus3");

EventoFocus1.addEventListener("focus",EventoFocus1_action);
EventoFocus2.addEventListener("focus",EventoFocus2_action);
EventoFocus3.addEventListener("focus",EventoFocus3_action);

EventoFocus1.addEventListener("blur",EventoBlur1_action);
EventoFocus2.addEventListener("blur",EventoBlur2_action);
EventoFocus3.addEventListener("blur",EventoBlur3_action);

function EventoFocus1_action(){
    EventoFocus1.style.background = "green"
}
function EventoFocus2_action(){
    EventoFocus2.style.background = "green"
}
function EventoFocus3_action(){
    EventoFocus3.style.background = "green"
}

//funciones para los eventos blur
function EventoBlur1_action(){
    EventoFocus1.style.background = "blue"
}
function EventoBlur2_action(){
    EventoFocus2.style.background = "blue"
}
function EventoBlur3_action(){
    EventoFocus3.style.background = "blue"
}

//ejercicios MouseOver
var EventoMouseOver1 = document.getElementById("EventoMouseOver1");
var EventoMouseOver2 = document.getElementById("EventoMouseOver2");
var EventoMouseOver3 = document.getElementById("EventoMouseOver3");

// eventos del MouseOver
EventoMouseOver1.addEventListener("mouseover",EventoMouseOver1_action);
EventoMouseOver2.addEventListener("mouseover",EventoMouseOver2_action);
EventoMouseOver3.addEventListener("mouseover",EventoMouseOver3_action);
EventoMouseOver1.addEventListener("mouseout",EventoMouseOut1_action);
EventoMouseOver2.addEventListener("mouseout",EventoMouseOut2_action);
EventoMouseOver3.addEventListener("mouseout",EventoMouseOut3_action);

function EventoMouseOver1_action(){
    EventoMouseOver1.textContent = "El puntero está sobre el elemento";
}
function EventoMouseOver2_action(){
    EventoMouseOver2.placeholder = "El puntero está sobre el elemento";
}
function EventoMouseOver3_action(){
    EventoMouseOver3.textContent = "El mouse está sobre del elemento";
}
function EventoMouseOut1_action(){
    EventoMouseOver1.textContent = "El puntero se retiró del elemento";
}
function EventoMouseOut2_action(){
    EventoMouseOver2.placeholder = "El puntero se retiró del elemento";
}
function EventoMouseOut3_action(){
    EventoMouseOver3.textContent = "El puntero se retiró del elemento";
}
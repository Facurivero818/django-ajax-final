const formulario = document.querySelector(".formulario");


// CREO EL TOKEN CSRFTOKEN DE MANERA CAMPERA SIN USAR LIBRERIA
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

// ESCUCHO EVENTO Y REALIZO FETCH
formulario.addEventListener("submit",async function(e){
    e.preventDefault()

    const datosFormulario = new FormData(formulario);
    const objetoFormulario = {};

     for (let [clave, valor] of datosFormulario.entries()) {
         objetoFormulario[clave] = valor;
     }

    const jsonFormulario = JSON.stringify(objetoFormulario);
    
    let peticion = await fetch("calculo", {
        method:"POST",
        body:jsonFormulario,
        headers: {'X-CSRFToken': csrftoken,
            // 'Content-Type': 'multipart/form-data'
          }}); 
    let resp = await peticion.json();
    console.log(resp);
    const respuesta = document.getElementById("resp");
    respuesta.textContent = resp["respuesta"];

});





document.addEventListener("DOMContentLoaded", function() {
    const especialidadDropdown = document.getElementById("especialidad");
    const medicoDropdown = document.getElementById("id_medico");

    especialidadDropdown.addEventListener("change", function() {
        const especialidadId = this.value;
        medicoDropdown.innerHTML = '<option value="">Cargando...</option>';

        if (especialidadId) {

            const url = `${window.location.origin}/turnos/filtrar-medicos/?especialidad_id=${especialidadId}`;

            fetch(url)
                .then(response => {
                    if (!response.ok) {
                        throw new Error(`HTTP error! Status: ${response.status}`);
                    }
                    return response.json();
                })
                .then(data => {
                    medicoDropdown.innerHTML = '<option value="">Seleccione un médico</option>';
                    data.forEach(medico => {
                        medicoDropdown.innerHTML += `<option value="${medico.user_id}">${medico.nombre_completo}</option>`; // Usamos medico.user_id
                    });
                })
                .catch(error => {
                    console.error("Error al cargar médicos:", error);
                    medicoDropdown.innerHTML = '<option value="">Error al cargar</option>';
                });
        } else {
            medicoDropdown.innerHTML = '<option value="">Seleccione un médico</option>';
        }
    });
});

document.addEventListener("DOMContentLoaded", function () {
    let errorContainer = document.getElementById("django-errors");
    let errorToastEl = document.getElementById("errorToast");
    let errorList = document.getElementById("error-list");

    if (errorContainer) {
        let errors = errorContainer.getAttribute("data-errors");

        if (errors) {
            let errorArray = errors.split("|").filter(e => e.trim() !== "");
            errorList.innerHTML = "";

            errorArray.forEach(error => {
                let li = document.createElement("li");
                li.textContent = error;
                errorList.appendChild(li);
            });

            let errorToast = new bootstrap.Toast(errorToastEl);
            errorToast.show();
        }
    }
});

// static/js/script.js (o como se llame tu archivo JS)

/**
 * Muestra una notificación Toast de Bootstrap.
 * @param {string} message - El mensaje a mostrar en el toast.
 * @param {string} [type='info'] - El tipo de toast ('success', 'error', 'warning', 'info'). Determina el color de fondo.
 */
function showToast(message, type = 'info') {
  const toastLiveExample = document.getElementById('liveToast');

  // Verifica si el elemento toast existe
  if (!toastLiveExample) {
    console.error('Elemento Toast con ID "liveToast" no encontrado.');
    return;
  }

  const toastBody = toastLiveExample.querySelector('.toast-body');

  // Verifica si el cuerpo del toast existe
  if (!toastBody) {
    console.error('Elemento ".toast-body" no encontrado dentro de #liveToast.');
    return;
  }

  // Actualiza el mensaje del toast
  toastBody.textContent = message;

  // Limpia clases de color anteriores y establece la nueva
  toastLiveExample.classList.remove('bg-success', 'bg-danger', 'bg-warning', 'bg-info', 'text-white');
  let bgClass = '';
  let textClass = 'text-dark'; // Color de texto por defecto

  switch (type.toLowerCase()) {
    case 'success':
      bgClass = 'bg-success';
      textClass = 'text-white'; // Texto blanco suele ir bien con éxito
      break;
    case 'error':
      bgClass = 'bg-danger';
      textClass = 'text-white'; // Texto blanco suele ir bien con error
      break;
    case 'warning':
      bgClass = 'bg-warning';
      textClass = 'text-dark'; // Texto oscuro suele ir bien con advertencia
      break;
    case 'info':
    default: // Por defecto será 'info'
      bgClass = 'bg-info';
      textClass = 'text-dark'; // Texto oscuro suele ir bien con info
      break;
  }

  if (bgClass) {
    toastLiveExample.classList.add(bgClass);
    // Añadir clase de texto si es necesario (ej. para fondos oscuros)
    if (textClass === 'text-white') {
        toastLiveExample.classList.add('text-white');
    }
  }


  // Intenta obtener la instancia de Toast de Bootstrap y mostrarla
  try {
    // Usa getOrCreateInstance para evitar problemas si se llama múltiples veces rápido
    const toast = bootstrap.Toast.getOrCreateInstance(toastLiveExample);
    toast.show();
  } catch (error) {
      console.error("Error al inicializar o mostrar el Toast de Bootstrap:", error);
      // Considera un fallback si Bootstrap no está cargado o falla
      // alert(message); // Fallback muy básico
  }
}

// Puedes añadir más código a tu script.js aquí si es necesario...

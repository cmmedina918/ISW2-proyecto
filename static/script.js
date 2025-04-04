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

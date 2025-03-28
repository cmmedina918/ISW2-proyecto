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
                        medicoDropdown.innerHTML += `<option value="${medico.id}">${medico.nombre}</option>`;
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


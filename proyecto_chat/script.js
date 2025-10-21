document.getElementById("enviar").addEventListener("click", enviarConsulta);

function enviarConsulta() {
  const input = document.getElementById("consulta");
  const mensaje = input.value.trim();
  const resultado = document.getElementById("resultado");

  if (mensaje === "") return;

  // Muestra el mensaje del usuario (verde)
  const msgUsuario = document.createElement("div");
  msgUsuario.classList.add("mensaje", "usuario");
  msgUsuario.textContent = mensaje;
  resultado.appendChild(msgUsuario);

  // Limpia el campo
  input.value = "";

  // Enviar al servidor
  fetch("/consulta", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ mensaje }),
  })
    .then((response) => response.json())
    .then((data) => {
      // Muestra la respuesta del bot (celeste)
      const msgBot = document.createElement("div");
      msgBot.classList.add("mensaje", "bot");
      msgBot.textContent = data.respuesta;
      resultado.appendChild(msgBot);
      resultado.scrollTop = resultado.scrollHeight;
    })
    .catch(() => {
      const msgError = document.createElement("div");
      msgError.classList.add("mensaje", "bot");
      msgError.textContent = "❌ Error al conectar con el servidor.";
      resultado.appendChild(msgError);
      resultado.scrollTop = resultado.scrollHeight;
    });
}

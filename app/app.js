let itens = JSON.parse(localStorage.getItem("itens")) || [];

function salvarDados() {
  localStorage.setItem("itens", JSON.stringify(itens));
}

function atualizarFormulario() {
  const categoria = document.getElementById("categoria").value;
  const form = document.getElementById("formCampos");
  form.innerHTML = "";

  if (!categoria) return;

  let campos = `
    <label>Marca:</label><input type="text" id="marca">
    ${categoria !== "Chip" ? `<label>Número de Patrimônio:</label><input type="text" id="numeroPatrimonio">` : ""}
    ${categoria === "Chip" ? `<label>DDD:</label><input type="text" id="ddd"> <label>Número:</label><input type="text" id="numeroLinha"> <label>Conta:</label><input type="text" id="conta">` : ""}
    <label>Serial:</label><input type="text" id="serial">
    ${categoria === "Computador" ? `<label>Etiqueta:</label><input type="text" id="etiqueta">` : ""}
    <label>Status:</label>
    <select id="status" onchange="mostrarCamposUsuario()">
      <option>Disponível</option>
      <option>Em uso</option>
      <option>Em manutenção</option>
    </select>
    <div id="camposUsuario">
      <label>Data de Recebimento:</label><input type="date" id="dataRecebimento">
      <label>Data de Entrega:</label><input type="date" id="dataEntrega">
      <label>Usuário Atual:</label><input type="text" id="usuarioAtual">
      <label>Unidade/Obra Atual:</label><input type="text" id="unidadeAtual">
      <label>Email do Funcionário:</label><input type="email" id="emailFuncionario">
      <label>Termo de Responsabilidade:</label>
      <select id="termo">
        <option>Cautelado no CRTI</option>
        <option>Aguardando cadastro do funcionário para cautelar</option>
      </select>
    </div>
    <label>Observação:</label><textarea id="observacao"></textarea>
  `;

  form.innerHTML = campos;
  mostrarCamposUsuario(); // aplica lógica inicial
}

function mostrarCamposUsuario() {
  const status = document.getElementById("status")?.value;
  const camposUsuario = document.getElementById("camposUsuario");
  if (status === "Disponível") {
    camposUsuario.classList.add("hidden");
  } else {
    camposUsuario.classList.remove("hidden");
  }
}

function adicionarItem() {
  const categoria = document.getElementById("categoria").value;
  if (!categoria) return alert("Selecione uma categoria!");

  const status = document.getElementById("status")?.value || "Disponível";

  const item = {
    id: Date.now(),
    categoria,
    marca: document.getElementById("marca")?.value || "",
    numeroPatrimonio: document.getElementById("numeroPatrimonio")?.value || "",
    ddd: document.getElementById("ddd")?.value || "",
    numeroLinha: document.getElementById("numeroLinha")?.value || "",
    conta: document.getElementById("conta")?.value || "",
    serial: document.getElementById("serial")?.value || "",
    etiqueta: document.getElementById("etiqueta")?.value || "",
    status,
    dataRecebimento: status !== "Disponível" ? document.getElementById("dataRecebimento")?.value : "",
    dataEntrega: status !== "Disponível" ? document.getElementById("dataEntrega")?.value : "",
    usuarioAtual: status !== "Disponível" ? document.getElementById("usuarioAtual")?.value : "",
    unidadeAtual: status !== "Disponível" ? document.getElementById("unidadeAtual")?.value : "",
    emailFuncionario: status !== "Disponível" ? document.getElementById("emailFuncionario")?.value : "",
    termo: status !== "Disponível" ? document.getElementById("termo")?.value : "",
    observacao: document.getElementById("observacao")?.value || "",
    antigosUsuarios: []
  };

  itens.push(item);
  salvarDados();
  atualizarTabela();
  document.getElementById("formCampos").innerHTML = "";
  document.getElementById("categoria").value = "";
}

function excluirItem(id) {
  itens = itens.filter(item => item.id !== id);
  salvarDados();
  atualizarTabela();
}

function abrirTransferencia(id) {
  const item = itens.find(i => i.id === id);
  const novoUsuario = prompt("Novo usuário:");
  if (!novoUsuario) return;
  const novaUnidade = prompt("Unidade/Obra do funcionário:");
  const novoEmail = prompt("Email do funcionário:");

  // guarda histórico
  if (item.usuarioAtual) {
    item.antigosUsuarios.push({
      nome: item.usuarioAtual,
      unidade: item.unidadeAtual,
      email: item.emailFuncionario
    });
  }

  item.usuarioAtual = novoUsuario;
  item.unidadeAtual = novaUnidade;
  item.emailFuncionario = novoEmail;

  salvarDados();
  atualizarTabela();
}

function atualizarTabela() {
  const tabela = document.getElementById("tabelaItens");
  tabela.innerHTML = "";
  itens.forEach(item => {
    tabela.innerHTML += `
      <tr>
        <td>${item.categoria}</td>
        <td>${item.marca}</td>
        <td>${item.numeroPatrimonio || item.numeroLinha || "-"}</td>
        <td>${item.serial || "-"}</td>
        <td>${item.etiqueta || "-"}</td>
        <td>${item.usuarioAtual || "-"}</td>
        <td>${item.unidadeAtual || "-"}</td>
        <td>${item.emailFuncionario || "-"}</td>
        <td>${item.status}</td>
        <td>${item.dataRecebimento || "-"}</td>
        <td>${item.dataEntrega || "-"}</td>
        <td>${item.termo || "-"}</td>
        <td>${item.observacao || "-"}</td>
        <td>
          <button class="btn-transf" onclick="abrirTransferencia(${item.id})">Transferir</button>
          <button class="btn-del" onclick="excluirItem(${item.id})">Excluir</button>
        </td>
      </tr>
    `;
  });
}

atualizarTabela();

function exportarJSON() {
  const dataStr = "data:text/json;charset=utf-8," + encodeURIComponent(JSON.stringify(itens, null, 2));
  const link = document.createElement("a");
  link.setAttribute("href", dataStr);
  link.setAttribute("download", "patrimonios.json");
  link.click();
}

function importarJSON(event) {
  const file = event.target.files[0];
  if (!file) return;
  const reader = new FileReader();
  reader.onload = function(e) {
    try {
      const dados = JSON.parse(e.target.result);
      if (Array.isArray(dados)) {
        itens = dados;
        salvarDados();
        atualizarTabela();
      } else {
        alert("Arquivo inválido!");
      }
    } catch {
      alert("Erro ao ler arquivo JSON!");
    }
  };
  reader.readAsText(file);
}

function exportarPDF() {
  const conteudo = document.querySelector("table").outerHTML;
  const janela = window.open("", "", "width=900,height=700");
  janela.document.write("<html><head><title>Relatório</title></head><body>");
  janela.document.write("<h1>Relatório de Patrimônios</h1>");
  janela.document.write(conteudo);
  janela.document.write("</body></html>");
  janela.document.close();
  janela.print();
}


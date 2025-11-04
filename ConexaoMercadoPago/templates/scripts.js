document.addEventListener('DOMContentLoaded', function () {
  const btnMain = document.getElementById('btn-olhar');   // botão que o usuário clica
  const btnFinal = document.getElementById('final-btn'); 

  if (!btnMain || !btnFinal) return;

  btnMain.addEventListener('click', function (e) {
    e.preventDefault();
    btnFinal.scrollIntoView({ behavior: 'smooth', block: 'center' });
    setTimeout(() => {
      try { btnFinal.focus({ preventScroll: true }); }
      catch (err) { btnFinal.focus(); }
    }, 450); 
  });
});
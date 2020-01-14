function get_afspraken() {
  fetch('http://127.0.0.1:5000/afspraken')
    .then((response) => {
      return response.json();
    })
    .then((afspraken) => {
      var table = document.getElementById('afspraken');
      let header = table.createTHead();
      var row = header.insertRow(0);
      var cell1 = row.insertCell(0);
      var cell2 = row.insertCell(1);
      cell1.innerHTML = '<strong>naam</strong>';
      cell2.innerHTML = '<strong>tijdstip</strong>';

      let body = table.createTBody();
      let c = 0;
      for (afspraak of afspraken) {
        console.log(afspraak);
        var row = body.insertRow();
        var cell1 = row.insertCell(0);
        var cell2 = row.insertCell(1);
        cell1.innerHTML = afspraak['naam'];
        cell2.innerHTML = afspraak['tijdstip'];
        c += 1;
      }
    });
}

function clear_afspraak() {
  document.getElementById('naam').value = '';
  document.getElementById('email').value = '';
  document.getElementById('tijdstip').value = '';
}

function set_afspraak_response(resp) {
  let response = document.getElementById('response');
  response.innerHTML = resp;
  if (resp = "") {
    response.style.display = 'none';
  } else {
    response.style.display = 'inline';
  }
}

function maak_afspraak() {
  let naam = document.getElementById('naam').value;
  if (naam == '') {
    set_afspraak_response('Geef een naam op....');
    return false;
  }

  let email = document.getElementById('email').value;
  if (email == '') {
    set_afspraak_response('Geef een email op....');
    return false;
  }

  let tijdstip = document.getElementById('tijdstip').value;
  if (tijdstip == '') {
    set_afspraak_response('Geef een tijdstip op....');
    return false;
  }

  set_afspraak_response('');

  let jsondata = { 'naam': naam, 'email': email, 'tijdstip': tijdstip };

  fetch('http://127.0.0.1:5000/afspraak', {
    method: 'POST',
    headers: { 'Accept': 'application/json', 'Content-Type': 'application/json' },
    body: JSON.stringify(jsondata)
  })
    .then((response) => {
      return response.json();
    })
    .then((result) => {
      if (!result['success']) {
        set_afspraak_response(
          'Probleem met het maken van een afspraak: ' + result['reason']);
      } else {
        set_afspraak_response('Afspraak is gemaakt!');
        clear_afspraak();
      }
    });
}
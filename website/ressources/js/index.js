$(document).ready(function() {
    $.ajax({
        url: 'http://localhost:5000/bossdata',
        method: 'POST', 
        contentType: 'application/json', 
        success: function(response) {
            console.log('Réponse du serveur:', response);
            addNewBoxes(response["boss"])
        },
        error: function(xhr, status, error) {
            console.error('Erreur:', error);
        }
    });
});


function addNewBoxes(response){
    const container = document.getElementById('cube-container');
    response.forEach(boss => {
        const cube = document.createElement('div');
        cube.classList.add('cube');
        container.appendChild(cube);
        const name = document.createElement('p');
        name.classList.add("name");
        name.innerText = boss["name"];
        const img = document.createElement('img');
        img.src = "ressources/img/boss/" + boss["img_link"]
        console.log(img.src)
        const level = document.createElement('p');
        level.classList.add("level");
        level.innerText = boss["level"];
        const stage = document.createElement('p')
        stage.innerText = "Étape " + boss["stage"]
        cube.appendChild(name);
        cube.appendChild(img);
        cube.appendChild(level);
        cube.appendChild(stage);
        cube.classList.add("notcaptured")
        cube.addEventListener("click", function(){
            cube.classList.toggle('captured')
        })
    });
}


function colorBox(event){
    event.target.style
}
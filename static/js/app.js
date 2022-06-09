var boton=document.getElementById('agregar');
var guardar=document.getElementById('guardar')
var lista=document.getElementById('lista')
var data=[];
var cant = 0;
boton.addEventListener('click', agreagar);
function agreagar(){
    var nombre=document.getElementById('nombre').value;
    var correo=document.getElementById('correo').value;
    var prioridades=document.getElementById('prioridades').value;
    var parcial=document.getElementById('parcial').value;

    //Agregar elementos al arreglo
    data.push(
        {       "id":cant,
                "nombre":nombre,
                "correo":correo,
                "prioridades":prioridades,
                "parcial":parcial

        }
    );
    var id_row='row'+cant;
    var fila='<tr id='+id_row+'><td>'+nombre+'</td><td>'+correo+'</td><td>'+prioridades+'</td><td>' + parcial +'</td></tr>';
    //Agregar a la tabla
    $("#lista").append(fila);
    $("#nombre").val('');
    $("#correo").val('');
    $("#prioridades").val('');
    $("#parcial").val('');
    $("#nombre").focus();
    cant++;

}
 
function save(){

}

function eliminar(row){

    //remover la fila  de la tabla html
    $("#row"+row).remove();
    var i = 0;
    var pos=0;
    for(x of data){
        if(x.id==row){
            pos=i;
        }
        i++;
    }
    data.splice(pos,1);
    


}


function sololetras(e){
    key=e.keyCode || e.which;

    tecaldo=String.fromCharCode(key).toLowerCase();

    letras = "abcdefgijklmnopqrstuvwxyz";
    especiales="8-37-38-46-164";

    teclado_especial = false;

    for(var i in especiales){
        if(key==especiales[1]){
            teclado_especial=true;break;

        }

    }
    if(letras.indexOf(teclado) ==-1 && !teclado_especial) {
        return false;

    }

}
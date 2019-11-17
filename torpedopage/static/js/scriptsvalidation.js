$(document).ready(function () {
  /*
      $.validator.setDefaults({
        errorClass:'error-label',
      highlight: function(element){
          $(element).addClass('error-control');
      },
      unhighlight: function(element){
      $(element).removeClass('error-control');
      }
    });
  */
  $("#mi-formulario").validate({
    rules: {
      email: {
        required: true,
        email: true
      },

    

      numtelefono: {
        customphone: true,
        required: false,
        maxlength: 14,
        minlength: 9,
      },

      name: {
        required: true,
        lettersonly: true
      },

      regiones: {
        required: true
      },

      comunas: {
        required: true
      },

      rut: {
        required: true,
        formatorut: true,
        verificardv: true
      },

      date: {
        required: true,
        mayoredad: true
      }
    },

    messages: {
      email: {
        required: 'Ingresa tu correo electrónico',
        email: 'Formato de correo no válido'
      },

   

      numtelefono: {
        /*required: 'Ingrese telefono',*/
        maxlength: 'Numero excede el maximo',
        minlength: 'Ingrese un numero de 9 digitos'
      },

      name: {
        required: 'Campo obligatorio',
        lettersonly: 'Solo letras'
      },

      regiones: {
        required: 'Campo obligatiorio'
      },

      comunas: {
        required: 'Campo obligatorio'
      },

      rut: {
        required: 'Campo obligatorio',
        formatorut: 'Formato rut no válido',
        verificardv: 'Rut no válido'
      },

      date: {
        required: 'Campo obligatorio',
        mayoredad: 'Edad Mínima 18 años'
      }
    }
  });
});

/*funcion para validar el rut con el digito verificador*/
function validarRut(rut){
  var suma = 0;
  var cuerpoRut = rut.substr(0, rut.length -1);
  var dv = rut.substr(rut.length -1).toUpperCase();
  var multiplicador = 2;
  /* suma la multiplicacion de cada numero que compone el rut */
  for (i = cuerpoRut.length -1; i >= 0; i--){
    suma = suma + (cuerpoRut.charAt(i) * multiplicador);
    if (multiplicador == 7){
      multiplicador = 2;
    }else{
      multiplicador++;
    }
  }
  /* divide la suma por 11 y obtiene el resto*/
  var resto = suma % 11;
  var verificadorDv;

  if (resto == 1){
    verificadorDv = 'K';
  }else{
    if(resto == 0){
      verificadorDv = '0';
    }else{
      verificadorDv = 11 - resto;
    }
  } 

  if (verificadorDv != dv){ return false; }
  else{ return true;}
}

/*valida la edad minima*/
function validarEdad(date){
  var hoy = new Date();
  var fechaNaci = new Date(date);
  var edadAnno = hoy.getFullYear() - fechaNaci.getFullYear();
  var edadMes = hoy.getMonth() - fechaNaci.getMonth();

  if (edadMes < 0 || (edadMes === 0 && hoy.getDate() < fechaNaci.getDate())){
    edadAnno--;
  }
  
  if (edadAnno >= 18){
    return true;
  }else{
    return false;
  }
}

$.validator.addMethod("mayoredad", function(value, element){
  return this.optional(element) || validarEdad(value);
}, "Edad Mínima 18 años");

$.validator.addMethod("verificardv", function(value, element){
  return this.optional(element) || validarRut(value);
}, "Rut no válido");

$.validator.addMethod('customphone', function (value, element) {
  return this.optional(element) || /^(\([+]\d{0})\)?|(\([56]\d{1})\)|(\([-]\d{0})\)?|(\([9]\d{0})\)?|(\([-]\d{0})\)?|\d{8}$/.test(value);
}, "Por favor ingrese un número de teléfono válido");


$.validator.addMethod("lettersonly", function (value, element) {
  return this.optional(element) || /^[a-z ]+$/i.test(value);
}, "Solo letras");

$.validator.addMethod("formatorut", function(value, element){
  return this.optional(element) || /^[0-9\d|kK]+$/.test(value);
}, "Formato rut no válido")

/*  /^(1-?)?(\([2-9]\d{2}\)|[2-9]\d{2})-?[2-9]\d{2}-?\d{4}$/    */



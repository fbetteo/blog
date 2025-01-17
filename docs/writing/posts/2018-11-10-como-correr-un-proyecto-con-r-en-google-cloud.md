---
title: 'Como correr un proyecto con R en Google Cloud '
authors:
  - fbetteo 
date: 2018-11-10
slug: como-correr-un-proyecto-con-r-en-google-cloud
categories:
  - R
tags:
  - R
  - Cloud
thumbnailImage: https://lh3.googleusercontent.com/IUeGbzdC2T2IIb_vrvmq3DOxtNOGnNafX0nYEmJhQktWDVn0Ej3MxaWEXqOKMm_WMnO50137sajv42E-lw=s192-rw
thumbnailImagePosition: left
summary: Post sobre como crear máquinas virtuales en Google Cloud y correr scripts de R en servidores alrededor del mundo!
---

# Como correr un proyecto con R en Google Cloud

Hay situaciones en que nuestras computadoras no alcanzan para correr ciertos algoritmos por la cantidad de memoria o núcleos que tenemos (y comprar otra no es una opción..). Una solución es correr nuestro proyecto en "la nube", es decir en servidores ajenos mantenidos por empresas. Los servicios de esta índole más conocidos son:


* Google Cloud
* Amazon AWS
* Microsoft Azure

En este post usaremos el primero. Como es de esperar, estos servicios son pagos y si su negocio lo amerita son una gran opción. Igualmente Google Cloud ofrece U$S300 de regalo al crear una cuenta por lo que podrían hacer uso para algún proyecto o pruebas. Les aseguro que no es particularmente bajo el monto. Solo tienen que registrarse y asociar una tarjeta de crédito y no abonar nada.

Google Cloud ofrece un montón de servicios y opciones de las cuales presentaremos lo más básico pero igualmente suficiente para correr un xgboost en gigas y gigas de datos con cientos de variables je. 

1. Crear una máquina virtual instalando R
2. Crear un Bucket que sirve como Disco duro para guardar data, outputs, etc
3. Correr un algoritmo

## Máquina Virtual


Una vez registrados, lo primero que vamos a hacer es crear la máquina virtual e instalar R y ciertos paquetes.
Lamentablemente el proceso es bastante engorroso para quienes no conocen bash ni están familiarizados con Cloud. Es todo por consola y para nada intuitivo sin leer la documentación, que está en inglés.
Es un proceso largo y la documentación más clara que encontré se encuentra en este [BLOG](http://grantmcdermott.com/2017/05/30/rstudio-server-compute-engine/). 
No tiene sentido intentar decir lo mismo que él pero peor. Les recomiendo seguirlo y van a obtener una máquina virtual con Rstudio instalado y ciertas dependencias útiles para la mayoría de las librerías que se usan.

<!-- lo tengo en la pc tambien por las dudas 
miran sino el dropbox https://www.dropbox.com/sh/8xzxv7erkeb3ncx/AADwqKGuOmXEPvy5pwNe7R1Ia/cloud?dl=0&subfolder_nav_tracking=1 -->

## Crear Bucket

Ir a 
![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/bucket1.PNG){width=200px height=350px}
Clickear los 3 puntos a la derecha y entrar a "Create key"

Se les descargará un archivo .json que deben renombrar a ** privatekey_inicial.json ** .
Luego ir a:
![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/bucket2.PNG){width=200px height=350px}

Crear un bucket cuyo nombre no tenga espacios ni caracteres raros. Va a pedirles que sea un nombre que no esté siendo usado por nadie más. 
Hecho esto el bucket está creado y se le pueden subir archivos. Luego desde los scripts también se le van a poder escribir directamente, es decir, guardar los outputs.
Ahora vamos a cambiar los permisos del bucket. Copiarse el account id desde aquí.
![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/bucket3.PNG){width=350px height=200px}

Luego ir a storage y en los 3 puntitos de nuesto bucket clickear "Edit Bucket permissions" y pegar el ID.
![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/bucket4.PNG){width=200px height=350px}

## Crear Imagen

Lo que haremos ahora es crear una imagen de la maquina virtual que generamos (donde instalamos R) para poder levantar futuras máquinas y que directamente tengan instalado R y los paquetes si lo deseamos (invocando a esta imagen).
Dejo imágenes de un tutorial que van a ser más claras que yo.

![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/imagen 1.PNG){width=400px height=700px}

![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/imagen2.PNG){width=400px height=700px}

![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/imagen3.PNG){width=400px height=700px}

Luego ir a Compute Engine --> Images



![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/imagen4.PNG){width=400px height=700px}

### Status

Resumiendo brevemente:

* Tenemos una cuenta y U$S 300 disponibles.
* Creamos una VM con R y paquetes.
* Generamos una imagen de esa VM para poder retutilizarla.
* Creamos un bucket donde almacenar inputs y outputs, linkeado a la imagen.

Estamos casi listos. Falta correr algun script!

## Cómo correr un script de R.

Una vez seteado todo lo anterior (y asegurándonos de haber apagado la maquina virtual utilizada) lo que debemos hacer es crear otras VM (instance) con los núcleos y Ram que cremos convenientes - esto depende totalmente de la complejidad del algoritmo que vayan a correr-, asignando una región donde preferentemente sea de noche o fin de semana para que esté menos saturada.
Lo más importante es cambiar el boot disk y seleccionar dentro de "custom" la imagen que hayamos generado con R. De esta manera la VM que iniciemos ya tendrá R, Rstudio y librerías instaladas.

![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/runscript1.PNG){width=200px height=350px}

Justo debajo de lo que se ve en la imagen hay opciones extras de "Management, security, disks", etc.
Depende la importancia de lo que estén haciendo puede ser bueno asegurarse que la opción *Preemptibility* esté OFF.
Si está ON, la VM se correrá en un servidor que máximo puede durar 24hs (posterior a eso se apaga automáticamente la VM) y más importante aún, están sujetos a disponibilidad de Google, es decir que si hay mucha demanda de servidores pueden apagarles el suyo sin consultar. Lo positivo es que son mucho más baratas.
Al tenerlo OFF, se aseguran que su VM estará encendida durante todo lo que tarde el script en correr y no va a depender de la demanda. Queda a criterio de cada uno.

Ya estamos listos para correr. Hay dos maneras sencillas:

1. **Directo desde Rstudio en la VM.**

Haciendo click en el IP de su instancia. Se abrirá Rstudio y deberán poner Usuario y Contraseña seteados durante la instalación.
Ahi pueden trabajar como si fuera directamente R. Recomiendo tener Script listo porque no es muy dinámico trabajar en vivo ahí.

![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/runscript2.PNG){width=200px height=350px}

2. **Desde la terminal, llamando a script en el bucket.**

Otra opción es subir su script al bucket que generaron y en Rstudio (como en 1.) ir a la terminal y correr:

```r
Rscipt --vanilla ~/cloud/cloud1/pathToScript/script.r
```

O desde la consola (que basicamente system() simular ser la temrinal) :

```r
system(Rscipt --vanilla ~/cloud/cloud1/pathToScript/script.r)
```

3. **Desde la terminal de la instancia.**

![](/post/2018-11-10-como-correr-un-proyecto-con-r-en-google-cloud_files/runscript3.PNG){width=200px height=350px}

Y ahí deberían poder correr sin problema.

```r
Rscipt --vanilla ~/cloud/cloud1/pathToScript/script.r
```

En cualquiera de los 3 casos presten atención a las rutas que usan en sus scripts para referenciar al bucket.
Si linkearon el bucket a la imagen de la VM como vimos en el post deberían poder usar la siguiente ruta genérica.


```r
"~/cloud/cloud1/RestoDelPath/"
```


Y eso es todo. Ya pueden levantar una VM en google cloud y correr algoritmos con gigas y gigas de data sin quemar su PC! 

---
title: "Como crear un blog con Blogdown y Netlify"
authors:
  - fbetteo 
date: 2018-10-07
slug: como-crear-un-blog-con-blogdown-y-netlify
thumbnailImage: https://lh3.googleusercontent.com/mQSV47CnAqm-l4jRnnOmNa1w9_FtRm4bN0L-YO7tfe32SzP0_bGZ3dJrvsbUEK2xkWMnZsSqXDc5VE2ukA=w190-h220-rw
tags:
- blogdown
- blog
- netlify
categories:
- R
- blog
thumbnailImagePosition: left
summary: Post sobre como poner en funcionamiento un blog utilizando Rstudio, blogdown, github y netlify! Todo gratis!
---

# Como crear un blog con Blogdown y Netlify

En este post vamos a ver el proceso reusmido para crear un blog donde podemos generar contenido directamente desde RStudio, utilizando el paquete [blogdown](https://bookdown.org/yihui/blogdown/), [Github](https://www.github.com) y [Netlify](https://www.netlify.com).
La idea es que al finalizar la configuración, simplemente creemos el post en Rstudio (un markdown) usando blogdown y que al subirlo a github automaticamente se actualice el blog y se vea reflejado en nuestra página. Es lo que estoy haciendo en este momento.

Lo primero y más importante más allá de este tema en particular es tener una cuenta en github. Si no la tienen se los recomiendo ampliamente para hacer version control - *actualizar código de forma segura y con backups constantes en un servidor + compartir proyectos*. Es gratis, al menos la versión básica que alcanza y sobra para el uso cotidiano. 
En nuestro repositorio crearemos un proyecto para el blog y ahi se subirán nuestros posts en formato html. A su vez, estará el theme y otras configuraciones básicas del blog.  

Lo segundo es instalar el paquete blogdown en nuestro R. Es una obra maestra de Yihui Xie, ingeniero de RStudio y creador de varios paquetes.
En un nuevo proyecto de R, ejecutan el siguiente comando.

```r
blogdown::new_site()
```

Con eso ya tienen generado la estructura básica de lo que será su blog. Se crearán carpetas y archivos en la ruta del proyecto con contenido de prueba para tener algo funcional.
Blogdown es bastante complejo y hay un millón de configuraciones y detalles que uno puede personalizar. No entraremos en eso acá porque se haría super extenso. Para eso está la [documentación oficial](https://bookdown.org/yihui/blogdown/) *en ingles*.

Eventualmente van a tener que cambiar el archivo config.toml con ciertos pasos de la guía y luego podrán explorar todas las posibilidades que presenta. Entre ellas pueden (y recomiendo) descargar otro theme para cambiar el formato. El que uso actualmente es [tranquilpeak](https://github.com/kakawait/hugo-tranquilpeak-theme).

Para crear un post nuevo simplemente escriben el comando.

```r
blogdown::new_post()
```

Lo cual genera un script con un YAML, que es la configuración con el título, tags y otros metadatos del post. Simplemente escriben como cualquier markdown debajo.
Cuando terminan el post (o mientras para ir visualizando como queda) corren 

```r
blogdown::serve_site()
```
Lo cual generará el archivo html correspondiente que luego será usado en su web y les permite ver el resultado temporal de su post.

Luego lo que deben hacer es pushear  la carpeta que se les generó del blog a su repositorio en github. O al menos las carpetas y archivos que se ven en la siguiente imagen. **Public** no la pusheen.

![gitsnap](/post/2018-10-07-como-crear-un-blog-con-blogdown-y-netlify/figure-html/GitSnapshot.PNG)


Llegado a este punto tenemos el contenido inicial del blog, pero no hay sitio web. Ahí es donde entra en juego Netlify.
No vamos a entrar en el paso a paso minucioso pero básicamente deben crearse una cuenta, generar una nueva web y linkearla a su repositorio Github. Es bastante lineal. Luego configuran el nombre de la web y otros detalles y en cuestión de minutos ya están publicados! (Y Gratis.)
Para ver bien esta etapa les recomiendo la explicación del link de blogdown.

Una vez puesto en marcha solo es cuestión de abrir su proyecto en R (en su pc), crear un nuevo post con blogdown::new_post() y pushear a github!
Prueben chusmeando todas las configuraciones para cambiar la estética del blog!

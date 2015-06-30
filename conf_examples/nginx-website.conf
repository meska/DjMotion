upstream django {
    server unix:///tmp/djmotion.sock;
    # server 127.0.0.1:8000;
}

upstream cam01 { server 127.0.0.1:48001; }
upstream cam02 { server 127.0.0.1:48002; }
upstream cam03 { server 127.0.0.1:48003; }
upstream cam04 { server 127.0.0.1:48004; }
upstream cam05 { server 127.0.0.1:48005; }
upstream cam06 { server 127.0.0.1:48006; }
upstream cam07 { server 127.0.0.1:48007; }
upstream cam08 { server 127.0.0.1:48008; }
upstream cam09 { server 127.0.0.1:48009; }
upstream cam10 { server 127.0.0.1:48010; }
upstream cam11 { server 127.0.0.1:48011; }
upstream cam12 { server 127.0.0.1:48012; }
upstream cam13 { server 127.0.0.1:48013; }

# configuration of the server
server {
    server_name cam.mecomsrl.com;
    charset     utf-8;

    # max upload size
    client_max_body_size 75M;


    # cams mjpeg stream
    
    location /stream/cam01 {  proxy_pass  http://cam01;  proxy_buffering off; }    
    location /stream/cam02 {  proxy_pass  http://cam02;  proxy_buffering off; }    
    location /stream/cam03 {  proxy_pass  http://cam03;  proxy_buffering off; }    
    location /stream/cam04 {  proxy_pass  http://cam04;  proxy_buffering off; }    
    location /stream/cam05 {  proxy_pass  http://cam05;  proxy_buffering off; }    
    location /stream/cam06 {  proxy_pass  http://cam06;  proxy_buffering off; }    
    location /stream/cam07 {  proxy_pass  http://cam07;  proxy_buffering off; }    
    location /stream/cam08 {  proxy_pass  http://cam08;  proxy_buffering off; }    
    location /stream/cam09 {  proxy_pass  http://cam09;  proxy_buffering off; }    
    location /stream/cam10 {  proxy_pass  http://cam10;  proxy_buffering off; }    
    location /stream/cam11 {  proxy_pass  http://cam11;  proxy_buffering off; }    
    location /stream/cam12 {  proxy_pass  http://cam12;  proxy_buffering off; }    
    location /stream/cam13 {  proxy_pass  http://cam13;  proxy_buffering off; }    

    # Django media
    location /media  {
        alias /home/operatore/DjMotion/media;
    }
    
    # Django static
    location /static {
        alias /home/operatore/DjMotion/static;
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass  django;
        include /home/operatore/DjMotion/djmotion/uwsgi_params;
    }
}

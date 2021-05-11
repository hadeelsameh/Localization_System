import 'package:flutter/material.dart';
import 'dart:async';
import 'package:dio/dio.dart';
void main() {
  runApp(MaterialApp(
    theme: ThemeData(
        primaryColor: Colors.pinkAccent, accentColor: Colors.lime
    ),
    debugShowCheckedModeBanner: false,
    home: Localization(),
  ));
}
class Localization extends StatefulWidget {
  // This widget is the root of your application.
  @override
  _LocalizationState createState() => _LocalizationState();
 }

class _LocalizationState  extends State<Localization> {
  @override
  void initState() {
    Timer.periodic(Duration(seconds: 10), (timer) {
      setState(() {});
    });
    super.initState();
  }
  @override
  Widget build(BuildContext context){
    return Scaffold(
      body:
      Container(
        decoration: BoxDecoration(
            image: DecorationImage(
              image: AssetImage("lib/img/SBME Map full.png"),
              fit: BoxFit.cover
            )
        ),
        width: 2000,
        height: 2000,
        child:  CustomPaint(
          painter: OpenPainter(),

    ),
    ),
    );
  }
}
class OpenPainter extends CustomPainter {
  var date = DateTime.now() ;
  //var a=110.00;
  //var b=200.00;
  int location;
  void getHttp() async {
    try {
      Response response = await Dio().get("https://api.thingspeak.com/channels/1207778/fields/1.json?results=2");
      String r = response.toString();
      //print(r);
      String filtered=r.substring(326 ,328);
      location=int.parse(filtered);
      print(location);
      if (location == 0) {
        vertical = 300;
        Horizontal=120;
      }else if (location == 1) {
        vertical = 310;
        Horizontal=210;
      }else if (location == 2) {
        vertical = 370;
        Horizontal=210;
      }else if (location == 3) {
        vertical = 600;
        Horizontal=210;
      }else if (location == 4) {
        vertical = 675;
        Horizontal=130;
      }else if (location == 5) {
        vertical = 520;
        Horizontal=210;
      }else if(location == 6 ){
        vertical = 510;
        Horizontal=110;
      }
      
    } catch (e) {
      print(e);
    }
  }
  @override
  void paint(Canvas canvas, Size size) {
    var paint1 = Paint()
      ..color = Colors.pink;
    //a circle
    double Horizontal;
    double vertical;
    var locate = getHttp();
    canvas.drawCircle(Offset(Horizontal, vertical), 10, paint1);
     }
  @override
  bool shouldRepaint(CustomPainter oldDelegate) => true;
  }


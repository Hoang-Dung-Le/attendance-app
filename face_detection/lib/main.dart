import 'package:camera/camera.dart';
import 'package:face_detection/face_detector.dart';
import 'package:flutter/material.dart';

List<CameraDescription> cameras = [];
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();

  cameras = await availableCameras();

  runApp(MaterialApp(
    home: Scaffold(body: FaceDetectorView()),
  ));
}

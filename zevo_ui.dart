import 'package:flutter/material.dart';

void main() => runApp(ZevoApp());

class ZevoApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        backgroundColor: Colors.green[50], // ZEVO's Green theme
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              Text(
                'ZEVO',
                style: TextStyle(fontSize: 40, fontWeight: FontWeight.bold, color: Colors.green[900]),
              ),
              Text('Zero Emission Vehicle Operator'),
              SizedBox(height: 50),
              Padding(
                padding: EdgeInsets.symmetric(horizontal: 40),
                child: TextField(
                  decoration: InputDecoration(
                    border: OutlineInputBorder(),
                    labelText: 'Enter Phone Number',
                  ),
                ),
              ),
              SizedBox(height: 20),
              ElevatedButton(
                style: ElevatedButton.styleFrom(backgroundColor: Colors.green),
                onPressed: () {
                  print("Login Attempted");
                },
                child: Text('Login to Drive'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

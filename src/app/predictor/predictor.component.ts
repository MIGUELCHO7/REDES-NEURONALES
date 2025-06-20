import { CommonModule } from '@angular/common';
import { HttpClient } from '@angular/common/http';
import { Component } from '@angular/core';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-predictor',
  imports: [FormsModule, CommonModule],
  templateUrl: './predictor.component.html',
  styleUrls: ['./predictor.component.css']
})
export class PredictorComponent {
  nombre: string = '';
  apellidos: string = '';
  edad: number | null = null;
peso: number | null = null;
estatura: number | null = null;
  resultado: string[] = [];

  constructor(private http: HttpClient) {}

  predecir() {
    const datos = {
      edad: this.edad,
      peso: this.peso,
      estatura: this.estatura
    };

    this.http.post<any>('http://localhost:5000/predict', datos).subscribe(
      response => {
        // El backend ahora devuelve solo un resultado string e IMC
        this.resultado = [`${response.resultado} (IMC: ${response.IMC})`];
        console.log('Respuesta del servidor:', this.resultado);
      },
      error => {
        console.error('Error al predecir:', error);
        this.resultado = ['Error al conectar con el servidor.'];
      }
    );
  }
}

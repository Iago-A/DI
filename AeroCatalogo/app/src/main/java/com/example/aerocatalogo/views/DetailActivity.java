package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.widget.Button;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import com.bumptech.glide.Glide;
import com.example.aerocatalogo.R;

public class DetailActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Obtener los datos pasados por el intent
        String title = getIntent().getStringExtra("plane_title");
        String description = getIntent().getStringExtra("plane_description");
        String url = getIntent().getStringExtra("plane_url");

        // Obtener referencias de las vistas
        TextView titleTextView = findViewById(R.id.titleTextView);
        ImageView imageView = findViewById(R.id.imageView);
        TextView descriptionTextView = findViewById(R.id.descriptionTextView);
        Button returnButton = findViewById(R.id.returnButton);

        // Establecer descripciones de accesibilidad.
        titleTextView.setContentDescription("Avión" + title);
        imageView.setContentDescription("Imagen del avión " + title);
        descriptionTextView.setContentDescription("Descripción: " + description);
        returnButton.setContentDescription("Volver a la lista de aviones");

        // Configurar botón de volver
        returnButton.setOnClickListener(v -> {
            finish();
        });

        // Asignar datos a las vistas
        titleTextView.setText(title);
        descriptionTextView.setText(description);

        // Cargar la imagen con Glide
        Glide.with(this)
                .load(url)
                .into(imageView);
    }
}

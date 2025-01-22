package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

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

        // Mostrar los datos en los TextViews (o donde los necesites)
        TextView titleTextView = findViewById(R.id.titleTextView);
        TextView descriptionTextView = findViewById(R.id.descriptionTextView);
        TextView urlTextView = findViewById(R.id.urlTextView);

        titleTextView.setText(title);
        descriptionTextView.setText(description);
        urlTextView.setText(url); // Mostrar la URL si la tienes
    }
}


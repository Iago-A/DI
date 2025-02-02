package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.bumptech.glide.Glide;
import com.example.aerocatalogo.R;
import com.example.aerocatalogo.viewmodels.FavoritesViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;

public class DetailActivity extends AppCompatActivity {
    private FloatingActionButton favoriteFab;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_detail);

        // Obtener los datos pasados por el intent
        String title = getIntent().getStringExtra("plane_title");
        String description = getIntent().getStringExtra("plane_description");
        String url = getIntent().getStringExtra("plane_url");
        String planeId = getIntent().getStringExtra("plane_id");

        FavoritesViewModel favoritesViewModel = new ViewModelProvider(this).get(FavoritesViewModel.class);

        // Obtener referencias de las vistas
        TextView titleTextView = findViewById(R.id.titleTextView);
        ImageView imageView = findViewById(R.id.imageView);
        TextView descriptionTextView = findViewById(R.id.descriptionTextView);
        FloatingActionButton returnFab = findViewById(R.id.returnFab);
        favoriteFab = findViewById(R.id.favoriteFab);
        View rootView = findViewById(android.R.id.content);

        // Establecer descripciones de accesibilidad.
        titleTextView.setContentDescription("Avión" + title);
        imageView.setContentDescription("Imagen del avión " + title);
        descriptionTextView.setContentDescription("Descripción: " + description);
        returnFab.setContentDescription("Volver a la lista de aviones");
        favoriteFab.setContentDescription("Añadir o eliminar de favoritos");

        // Configurar botón de volver
        returnFab.setOnClickListener(v -> {
            finish();
        });

        // Asignar datos a las vistas
        titleTextView.setText(title);
        descriptionTextView.setText(description);

        // Cargar la imagen con Glide
        Glide.with(this)
                .load(url)
                .into(imageView);

        // Observar estado favorito
        favoritesViewModel.isFavorite(planeId).observe(this, isFavorite ->
                updateFabIcon(isFavorite)
        );

        favoriteFab.setOnClickListener(v ->
            favoritesViewModel.toggleFavorite(planeId)
        );

        // Observar cambios y mostrar Snackbar
        favoritesViewModel.getFavoriteActionStatus().observe(this, isFavorite -> {
            String message = isFavorite ?
                    "Añadido a favoritos" :
                    "Eliminado de favoritos";

            Snackbar.make(rootView, message, Snackbar.LENGTH_SHORT).show();
        });
    }

    private void updateFabIcon(boolean isFavorite) {
        favoriteFab.setImageResource(
                isFavorite ? R.drawable.baseline_star_24 : R.drawable.baseline_star_border_24
        );
    }
}

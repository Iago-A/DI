package com.example.aerocatalogo.views;

import android.os.Bundle;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.adapters.FavoritesAdapter;
import com.example.aerocatalogo.viewmodels.FavoritesViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

import java.util.ArrayList;

public class FavoritesActivity extends AppCompatActivity {
    private FavoritesViewModel favoritesViewModel;
    private FavoritesAdapter adapter;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_favorites);

        // Configurar RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recyclerFavorites);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Inicializar adapter con lista vacía
        adapter = new FavoritesAdapter(new ArrayList<>());
        recyclerView.setAdapter(adapter);

        // Configurar ViewModel
        favoritesViewModel = new ViewModelProvider(this).get(FavoritesViewModel.class);

        // Obtener referencias de las vistas
        FloatingActionButton returnFab = findViewById(R.id.returnFab);

        // Establecer descripciones de accesibilidad.
        returnFab.setContentDescription("Volver");

        // Configurar botón volver
        returnFab.setOnClickListener(v -> {
            finish();
        });

        // Observar cambios en la lista de aviones
        favoritesViewModel.getFavorites().observe(this, favorites ->
                adapter.updateFavorites(favorites)
        );
    }
}

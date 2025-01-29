package com.example.aerocatalogo.views;

import android.content.Intent;
import android.os.Bundle;
import android.widget.Button;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;
import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.adapters.PlaneAdapter;
import com.example.aerocatalogo.models.Plane;
import com.example.aerocatalogo.viewmodels.DashboardViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.firebase.auth.FirebaseAuth;

import java.util.ArrayList;


public class DashboardActivity extends AppCompatActivity {

    private DashboardViewModel viewModel;
    private PlaneAdapter adapter;
    private FirebaseAuth mAuth;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_dashboard);

        // Inicializar FirebaseAuth
        mAuth = FirebaseAuth.getInstance();

        // Configurar RecyclerView
        RecyclerView recyclerView = findViewById(R.id.recyclerView);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        // Inicializar adapter con lista vacía
        adapter = new PlaneAdapter(new ArrayList<>(), this::openDetailActivity);
        recyclerView.setAdapter(adapter);

        // Configurar ViewModel
        viewModel = new ViewModelProvider(this).get(DashboardViewModel.class);

        // Observar cambios en la lista de aviones
        viewModel.getPlanes().observe(this, planes -> {
            adapter = new PlaneAdapter(planes, this::openDetailActivity);
            recyclerView.setAdapter(adapter);
        });

        // Observar errores
        viewModel.getError().observe(this, error -> {
            if (error != null) {
                Toast.makeText(this, error, Toast.LENGTH_LONG).show();
            }
        });

        // Configurar botón de logout
        FloatingActionButton logoutFab = findViewById(R.id.logoutFab);
        logoutFab.setContentDescription("Cerrar sesión");
        logoutFab.setOnClickListener(v -> {
            // Limpiar ViewModel
            getViewModelStore().clear();
            mAuth.signOut();
            Toast.makeText(this, "Logout correctly", Toast.LENGTH_SHORT).show();
            startActivity(new Intent(this, LoginActivity.class));
            finish();
        });

        // Configurar botón de configuración
        FloatingActionButton settingsFab = findViewById(R.id.settingsFab);
        settingsFab.setContentDescription("Abrir configuración");
        settingsFab.setOnClickListener(v -> {
            try {
                Intent intent = new Intent(DashboardActivity.this, SettingsActivity.class);
                startActivity(intent);
            } catch (Exception e) {
                Toast.makeText(this, "Error al abrir configuraciones", Toast.LENGTH_SHORT).show();
                e.printStackTrace();
            }
        });
    }

    private void openDetailActivity(Plane plane) {
        Intent intent = new Intent(this, DetailActivity.class);
        intent.putExtra("plane_title", plane.getTitle());
        intent.putExtra("plane_description", plane.getDescription());
        intent.putExtra("plane_url", plane.getUrl());
        startActivity(intent);
    }
}
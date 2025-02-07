package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.widget.Switch;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.viewmodels.SettingsViewModel;
import com.google.android.material.floatingactionbutton.FloatingActionButton;

public class SettingsActivity extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        SettingsViewModel settingsViewModel = new ViewModelProvider(this).get(SettingsViewModel.class);

        // Obtener referencias de las vistas
        TextView textView = findViewById(R.id.textView);
        Switch darkModeSwitch = findViewById(R.id.darkModeSwitch);
        FloatingActionButton returnFab = findViewById(R.id.returnFab);

        // Establecer descripciones de accesibilidad
        textView.setContentDescription("Modo oscuro");
        darkModeSwitch.setContentDescription("Activar o desactivar modo oscuro");
        returnFab.setContentDescription("Volver");

        // Observar el estado del modo oscuro
        settingsViewModel.getDarkModeLiveData().observe(this, darkModeSwitch::setChecked);

        // Configurar switch
        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            // Aplicar el tema inmediatamente
            settingsViewModel.setDarkMode(isChecked);
        });

        // Configurar botón de volver
        returnFab.setOnClickListener(v -> {
            finish();
        });
    }
}

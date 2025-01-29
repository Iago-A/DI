package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.widget.Switch;
import android.widget.Toast;

import androidx.appcompat.app.AppCompatActivity;
import androidx.appcompat.app.AppCompatDelegate;
import androidx.lifecycle.ViewModelProvider;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.viewmodels.SettingsViewModel;

public class SettingsActivity extends AppCompatActivity {
    private SettingsViewModel settingsViewModel;
    private Switch darkModeSwitch;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        // Inicializar ViewModel de primero
        settingsViewModel = new ViewModelProvider(this).get(SettingsViewModel.class);

        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        // Inicializar vistas
        darkModeSwitch = findViewById(R.id.darkModeSwitch);

        // Cargar el estado guardado
        darkModeSwitch.setChecked(settingsViewModel.isDarkModeEnabled());

        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            settingsViewModel.saveDarkModePreference(isChecked);
            // Aplicar el tema inmediatamente
            AppCompatDelegate.setDefaultNightMode(
                    isChecked ? AppCompatDelegate.MODE_NIGHT_YES : AppCompatDelegate.MODE_NIGHT_NO
            );
        });
    }
}

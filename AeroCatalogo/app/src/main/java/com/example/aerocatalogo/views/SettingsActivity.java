package com.example.aerocatalogo.views;

import android.os.Bundle;
import android.widget.Switch;

import androidx.appcompat.app.AppCompatActivity;
import androidx.lifecycle.ViewModelProvider;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.viewmodels.SettingsViewModel;

public class SettingsActivity extends AppCompatActivity {
    private SettingsViewModel settingsViewModel;
    private Switch darkModeSwitch;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_settings);

        settingsViewModel = new ViewModelProvider(this).get(SettingsViewModel.class);

        // Inicializar vistas
        darkModeSwitch = findViewById(R.id.darkModeSwitch);

        // Observar el estado del modo oscuro
        settingsViewModel.getDarkModeLiveData().observe(this, darkModeSwitch::setChecked);

        darkModeSwitch.setOnCheckedChangeListener((buttonView, isChecked) -> {
            // Aplicar el tema inmediatamente
            settingsViewModel.setDarkMode(isChecked);
        });
    }
}

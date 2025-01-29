package com.example.aerocatalogo.viewmodels;

import android.app.Application;
import android.content.Context;
import android.content.SharedPreferences;

import androidx.lifecycle.AndroidViewModel;

public class SettingsViewModel extends AndroidViewModel {
    private static final String PREFS_NAME = "AppConfig";
    private static final String DARK_MODE_KEY = "darkMode";
    private final SharedPreferences sharedPreferences;

    public SettingsViewModel(Application application) {
        super(application);
        sharedPreferences = getApplication().getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
    }

    // Obtener la preferencia del modo oscuro
    public boolean isDarkModeEnabled() {
        return sharedPreferences.getBoolean(DARK_MODE_KEY, false);
    }

    // Guardar el estado del modo oscuro
    public void saveDarkModePreference(boolean isEnabled) {
        SharedPreferences.Editor editor = sharedPreferences.edit();
        editor.putBoolean(DARK_MODE_KEY, isEnabled);
        editor.apply();
    }
}

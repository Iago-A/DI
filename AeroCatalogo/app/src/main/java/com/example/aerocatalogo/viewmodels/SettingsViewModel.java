package com.example.aerocatalogo.viewmodels;

import android.app.Application;
import android.content.Context;
import android.content.SharedPreferences;

import androidx.appcompat.app.AppCompatDelegate;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;


public class SettingsViewModel extends AndroidViewModel {
    private static final String PREFS_NAME = "AppConfig";
    private static final String KEY_DARK_MODE = "darkMode";
    private final SharedPreferences sharedPreferences;
    private final MutableLiveData<Boolean> darkModeLiveData = new MutableLiveData<>();

    public SettingsViewModel(Application application) {
        super(application);
        sharedPreferences = application.getSharedPreferences(PREFS_NAME, Context.MODE_PRIVATE);
        darkModeLiveData.setValue(sharedPreferences.getBoolean(KEY_DARK_MODE, false));
    }

    public LiveData<Boolean> getDarkModeLiveData() {
        return darkModeLiveData;
    }

    public void setDarkMode(boolean isEnabled) {
        sharedPreferences.edit().putBoolean(KEY_DARK_MODE, isEnabled).apply();
        darkModeLiveData.setValue(isEnabled);
        applyDarkMode(isEnabled);
    }

    private void applyDarkMode(boolean enable) {
        if (enable) {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_YES);
        } else {
            AppCompatDelegate.setDefaultNightMode(AppCompatDelegate.MODE_NIGHT_NO);
        }
    }
}


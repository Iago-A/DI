package com.example.aerocatalogo.viewmodels;

import android.app.Application;
import android.util.Log;

import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;

import com.example.aerocatalogo.models.Favorite;
import com.example.aerocatalogo.repositories.FavoritesRepository;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

import java.util.List;

public class FavoritesViewModel extends AndroidViewModel {
    private FavoritesRepository favoritesRepository;
    private String userId;

    public FavoritesViewModel(Application application) {
        super(application);
        FirebaseUser currentUser = FirebaseAuth.getInstance().getCurrentUser();
        userId = currentUser != null ? currentUser.getUid() : "";
        favoritesRepository = new FavoritesRepository(userId);
    }

    public LiveData<List<Favorite>> getFavorites() {
        return favoritesRepository.getFavorites();
    }

    public LiveData<Boolean> isFavorite(String planeId) {
        return favoritesRepository.isFavorite(planeId);
    }

    public void toggleFavorite(String elementId) {
        favoritesRepository.toggleFavorite(elementId)
                .addOnCompleteListener(task -> {
                    if (!task.isSuccessful()) {
                        Log.e("FavoritesViewModel", "Error toggling favorite", task.getException());
                    }
                });
    }
}

package com.example.aerocatalogo.viewmodels;

import android.app.Application;
import android.util.Log;

import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.MutableLiveData;

import com.example.aerocatalogo.models.Favorite;
import com.example.aerocatalogo.repositories.FavoritesRepository;
import com.google.firebase.auth.FirebaseAuth;
import com.google.firebase.auth.FirebaseUser;

import java.util.List;

public class FavoritesViewModel extends AndroidViewModel {
    private final MutableLiveData<Boolean> favoriteActionStatus = new MutableLiveData<>();
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

    // Getter para el LiveData
    public LiveData<Boolean> getFavoriteActionStatus() {
        return favoriteActionStatus;
    }

    public void toggleFavorite(String planeId) {
        favoritesRepository.toggleFavorite(planeId)
                .addOnCompleteListener(task -> {
                    if (task.isSuccessful()) {
                        // Actualizamos el LiveData con el nuevo estado (para el snackbar)
                        favoriteActionStatus.setValue(task.getResult());
                    }
                    else {
                        Log.e("FavoritesViewModel", "Error toggling favorite", task.getException());
                    }
                });
    }
}

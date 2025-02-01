package com.example.aerocatalogo.adapters;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import com.example.aerocatalogo.R;
import com.example.aerocatalogo.models.Favorite;

import java.util.List;

public class FavoritesAdapter extends RecyclerView.Adapter<FavoritesAdapter.FavoriteViewHolder> {
    private List<Favorite> favorites;

    public FavoritesAdapter(List<Favorite> favorites) {
        this.favorites = favorites;
    }

    public void updateFavorites(List<Favorite> newFavorites) {
        this.favorites = newFavorites;
        notifyDataSetChanged();
    }

    @NonNull
    @Override
    public FavoriteViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext())
                .inflate(R.layout.item_favorite, parent, false);
        return new FavoriteViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull FavoriteViewHolder holder, int position) {
        holder.bind(favorites.get(position));
    }

    @Override
    public int getItemCount() {
        return favorites.size();
    }

    static class FavoriteViewHolder extends RecyclerView.ViewHolder {
        private TextView favoriteNameTextView;

        public FavoriteViewHolder(@NonNull View itemView) {
            super(itemView);
            favoriteNameTextView = itemView.findViewById(R.id.planeTitle);
        }

        public void bind(Favorite favorite) {
            favoriteNameTextView.setText(favorite.getId());
        }
    }
}

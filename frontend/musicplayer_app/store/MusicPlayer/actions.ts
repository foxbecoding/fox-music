import { MusicPlayerState} from '~/store/MusicPlayer';
import { ActionTree } from 'vuex';
import { RootState } from '~/store';
import {currentSongIndex} from '@/store/MusicPlayer/methods';
import Song from '~/utils/types/Songs';

export const actions: ActionTree<MusicPlayerState, RootState> = {
    loop({state, commit}): void {
      if(!state.audio.loop){
          state.audio.loop = true;
          commit('isLoop', true as boolean);
          return;
      }
      state.audio.loop = false;
      commit('isLoop', false as boolean);
    },
    mute({state, commit}): void {
      if(!state.audio.muted){
        state.audio.muted = true;
        commit('isMuted', true as boolean);
        return;
      }
      state.audio.muted = false;
      commit('isMuted', false as boolean);
    },
    nextSong({state, commit}): void {
      let current_song_index: number = currentSongIndex(state);
      if(current_song_index < state.songs.length - 1){
          let song_index: number = current_song_index + 1;
          let song: Song = state.songs[song_index];
          commit('song', song as Song);
          commit('audio', `/assets/songs/${song.filename}` as string);
          return;
      } 
    },
    play_pause({state, commit}): void  {
      if(!state.audio.paused){
        state.audio.pause();
        commit('isPaused', true as boolean);
        return;
      }
      state.audio.play();
      commit('isPaused', false as boolean);
    },
    prevSong({state, commit}): void {
      let current_song_index = currentSongIndex(state);
      if(state.currentTime > 3){
          state.audio.currentTime = 0 as number;
          return;
      }
      if(current_song_index > 0){
          let song_index: number = current_song_index - 1;
          let song: Song = state.songs[song_index];
          commit('song', song as Song);
          commit('audio', `/assets/songs/${song.filename}` as string);
      } 
    },
    shuffle({state, commit}): void {
      if(!state.isShuffled){
          let new_songs_list: Array<Song> = [...state.songs];
          new_songs_list.sort(() => Math.random() - 0.5);
          new_songs_list.forEach((song: Song, i: number): void => {
              if(song.uniqid === state.song.uniqid){
                  new_songs_list.splice(i, 1);
                  new_songs_list.unshift(song);
              }
          });
          commit('songs', new_songs_list);
          commit('isShuffled', true);
          return;
      }
      commit('songs', state.songsConst);
      commit('isShuffled', false);
    },
    volume({state, commit}, vol: number): void { 
        let volume = vol/100
        state.audio.volume = volume;
        commit('volume', volume)
    }
  };

  export default actions
import { MusicPlayerState} from '~/store/MusicPlayer';
import { MutationTree } from 'vuex';
import { timeFormat} from '@/store/MusicPlayer/methods';
import Song from '~/utils/types/Songs';

const mutations: MutationTree<MusicPlayerState> = {
    audio(state: MusicPlayerState, audio_file: string): void{
      if(state.audio != null){
        state.audio.src = ""
        state.audio = null
      }
      state.audio = new Audio(audio_file)
      state.isPaused = false;
      state.audio.muted = state.isMuted;
      state.audio.loop = state.isLoop;
      state.audio.volume = state.volume;
      state.isEnded = state.audio.ended; 
      state.audio.load();
      state.audio.play();
    },
  
    duration(state: MusicPlayerState, data: number): void{
      state.duration = data
      state.durationStr = timeFormat(data)
    },
  
    currentTime(state: MusicPlayerState, data: number): void{
      state.currentTime = data
      state.currentTimeStr = timeFormat(data)
    },
  
    currentTimeStr(state: MusicPlayerState, data: number): void{
      state.currentTimeStr = timeFormat(data)
    },
  
    isActive(state: MusicPlayerState, data: boolean): void{
      state.isActive = data
    },
  
    isEnded(state: MusicPlayerState, data: boolean): void{
      state.isEnded = data
    },
  
    isLoop(state: MusicPlayerState, data: boolean): void {
      state.isLoop = data
    },
  
    isMuted(state: MusicPlayerState, data: boolean): void {
      state.isMuted = data
    },
  
    isPaused(state: MusicPlayerState, data: boolean): void {
      state.isPaused = data
    },
  
    isSliding(state: MusicPlayerState, data: boolean): void {
      state.isSliding = data
    },
  
    isShuffled(state: MusicPlayerState, data: boolean): void {
      state.isShuffled = data
    },
  
    song(state: MusicPlayerState, song: Song): void {
      state.song = song
    },
  
    songs(state: MusicPlayerState, songs: Song[]): void {
      state.songs = songs
    },
  
    songsConst(state: MusicPlayerState, songsConst: Song[]): void {
      state.songsConst = songsConst
    },
    volume(state: MusicPlayerState, data: number): void {
      state.volume = data
    }
};

export default mutations

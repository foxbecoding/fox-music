import MusicPlayer from '@/store/MusicPlayer/types';
import Song from '~/utils/types/Songs';

export const state = () => ({
  audio: null,
  currentTime: 0,
  currentTimeStr: '0:00', 
  duration: 0,
  durationStr: '',
  isActive: false,
  isEnded: false,
  isLoop: false,
  isMuted: false,
  isPaused: true,
  isSliding: false,
  isShuffled: false,
  song: {} as Song,
  songs: [] as Song[],
  songsConst: [] as Song[],
  volume: 1,
} as MusicPlayer);

export type MusicPlayerState = ReturnType<typeof state>
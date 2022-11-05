import Song from '@/utils/types/Songs';

interface MusicPlayer {
    audio: any;
    currentTime: number;
    currentTimeStr: string; 
    duration: number;
    durationStr: string;
    isActive: boolean;
    isEnded: boolean;
    isLoop: boolean;
    isMuted: boolean;
    isPaused: boolean;
    isSliding: boolean;
    isShuffled: boolean;  
    song: Song;
    songs: Song[];
    songsConst: Song[];
    volume: number;
}

export default MusicPlayer 